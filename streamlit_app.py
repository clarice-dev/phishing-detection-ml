import streamlit as st
import joblib
import numpy as np
import tldextract
import urllib.parse
import socket

# Load the model
model = joblib.load('random_forest_reduced_model.pkl')

# Feature Extractor. 
def extract_features_from_url(url):
    features = []

# Helper Function
# Checks if the domain part of the URL is an IP address (e.g. http://192.168.1.1)
    def is_ip(url):
      try:
        result = urllib.parse.urlparse(url)
        host = result.netloc
        socket.inet_aton(host)
        return 1
      except:
        return 0
# This is where we are extracting all the features of the 
# url that would help us know whether the url is legit or phishing scam.
# Done 1-13, 13-30 are default

# Feature 1: UsingIP
# We call the helper function to get the actual feature value
    features.append(is_ip(url))

# Feature 2: LongURL (length > 75)
    features.append(1 if len(url) >= 75 else 0)

# Feature 3: ShortURL (using bit.ly, tinyurl etc.)
    shorteners = ['bit.ly', 'goo.gl', 'tinyurl', 'ow.ly']
    features.append (1 if any(short in url for short in shorteners)else 0)

# Feature 4: Symbol@
    features.append(1 if '@' in url else 0)

# Feature 5: Redirecting//
    features.append(1 if url.count('//') > 1 else 0)

# Feature 6: PrefixSuffix-
    ext = tldextract.extract(url)
    features.append(1 if '-' in ext.domain else 0)

# Feature 7: Subdomains (many subdomains)
    domain_parts = ext.subdomain.split('.')
    features.append(1 if len(domain_parts) > 2 else 0)

# Feature 8: HTTPS
    features.append(1 if url.startswith('http') else 0)

# Feature 9: DomainRegLen (hard to check without WHOIS → placeholder)
    features.append(0) # Requires WHOIS, set default for now

# Feature 10: Favicon (not available from URL → default)
    features.append(0) # Requires favicon, set default for now

# Feature 11: NonStdPort
    parsed = urllib.parse.urlparse(url)
    features.append(1 if parsed.port and parsed.port not in [80, 443] else 0)

# Feature 12: HTTPSDomainURL (https but not matching domain)
    features.append(1 if 'https' in url and not url.startswith('https://'+ext.domain) else 0)

# Feature 13:
    features.append(0)  # Dummy feature 13
    return np.array([features])


# Streamlit User Interface
st.title("🔎 Phishing URL Detector")
url_input = st.text_input("Enter a website URL:")

# Checks if url is entered to avoid errors from empty input.
if url_input: 
    features = extract_features_from_url(url_input)
    st.write("🔍 Extracted features:", features)
    st.write("🧩 Shape of features:", np.shape(features))
    st.write("🧪 Extracted feature vector:", features)
    prediction = model.predict(features)[0] # prediction of  whether url is phishing or legit
    confidence = model.predict_proba(features)[0][prediction] # Gets confidence level

    if prediction == 1:
        st.error(f"⚠️ Phishing detected ({confidence*100:.2f}% confidence)")
    else:
        st.success(f"✅ Legitimate URL ({confidence*100:.2f}% confidence)")