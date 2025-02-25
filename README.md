# ElGamal Digital Signature (EDS)

This project implements the **ElGamal Digital Signature Scheme** using Python. It includes core cryptographic algorithms such as the **Miller-Rabin Primality Test**, **Euclidean Algorithm (EA)**, **Extended Euclidean Algorithm (EEA)**, **Square and Multiply Algorithm (SM)**, and the complete **ElGamal key generation, signing, and verification process**.

## 📁 Project Repository  
🔗 **GitHub Link:** [ELGAMALDIGITALSIG](https://github.com/Noraize/ELGAMALDIGITALSIG)  
📄 **Source Code File:** [`EDS.py`](https://github.com/Noraize/ELGAMALDIGITALSIG/blob/main/EDS.py)

---

## 🚀 Features
✅ Generate large prime numbers using Miller-Rabin Primality Test (512-bit prime generation)  
✅ Compute GCD using Euclidean Algorithm (EA)  
✅ Find modular inverses with Extended Euclidean Algorithm (EEA)  
✅ Perform fast modular exponentiation using the Square and Multiply (SM) algorithm  
✅ Generate ElGamal public-private key pairs  
✅ Sign messages with ElGamal digital signatures  
✅ Verify signatures for integrity and authenticity  

---

## 💻 Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Noraize/ELGAMALDIGITALSIG.git
   cd ELGAMALDIGITALSIG
   ```
2. **Run the Code:**
   ```bash
   python EDS.py
   ```

_No additional dependencies are required as the project uses Python’s standard libraries._

---

## ⚙️ Usage
1. **Key Generation:** Generates a 512-bit prime and computes the ElGamal key pair.
2. **Signing:** Signs a given message using the private key.
3. **Verification:** Verifies the signature using the public key.

You can modify the `message` variable in `EDS.py` to sign and verify different messages.

---

## 📊 Algorithms Implemented
### 1. Miller-Rabin Primality Test  
Efficient probabilistic test to check the primality of large numbers.

### 2. Euclidean Algorithm (EA)  
Finds the Greatest Common Divisor (GCD) of two integers.

### 3. Extended Euclidean Algorithm (EEA)  
Computes the modular inverse crucial for digital signatures.

### 4. Square and Multiply (SM) Algorithm  
Performs fast modular exponentiation.

### 5. ElGamal Digital Signature  
- **Key Generation:** Creates public and private keys.
- **Signing:** Produces a signature `(r, s)` for a message.
- **Verification:** Confirms the validity of the signature.

---

## 📦 Example Output
```
ElGamal key pair:
p: 130487... (512-bit prime)
alpha: 109857...
Public key: 754632...
Private key: 456281...

Signature:
r: 678932...
s: 329871...

Is the signature valid? True
```

---

## 📚 References
- [ElGamal Digital Signature - Wikipedia](https://en.wikipedia.org/wiki/ElGamal_signature_scheme)  
- "Cryptography and Network Security" by William Stallings  
- [Miller–Rabin Primality Test - GeeksforGeeks](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)  

---

## 🤝 Contributing
Pull requests are welcome! Feel free to open issues or submit feature requests.

---


🚀 Happy Cryptographing! 🔒

