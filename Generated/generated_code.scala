Here is the C++ code that implements the Needham-Schroeder protocol as described in the protocol draft:
```cpp
#include <iostream>
#include <string>

// Define a struct to represent a message
struct Message {
    std::string sender;
    std::string receiver;
    std::string contents;
};

class Alice {
public:
    void initiateSession(Message& message) {
        // Generate nonce and identity
        std::string na = "nonce_a";
        std::string identity = "alice";

        // Encrypt message with Bob's public key
        std::string encryptedMessage = encrypt(na, message.receiver, publicKey);

        // Send message to Bob
        std::cout << "Alice sends: " << encryptedMessage << std::endl;
    }

    void receiveMessage(Message& message) {
        // Decrypt message from Bob
        std::string decryptedMessage = decrypt(message.contents, message.sender, myPublicKey);

        // Extract nonce and identity from decrypted message
        std::string nb = extractNonce(decryptedMessage);
        std::string bobIdentity = extractIdentity(decryptedMessage);

        // Check if nonce matches
        if (nb == na) {
            // Send back encrypted message with Bob's nonce
            std::string encryptedResponse = encrypt(nb, bobIdentity, publicKey);
            std::cout << "Alice sends: " << encryptedResponse << std::endl;
        } else {
            std::cout << "Nonce mismatch!" << std::endl;
        }
    }

private:
    std::string myPublicKey;
    std::string na;

    // Function to encrypt a message with a public key
    std::string encrypt(std::string nonce, std::string receiver, std::string publicKey) {
        // This is a placeholder function and should be replaced with actual encryption logic
        return "encrypted_message";
    }

    // Function to decrypt a message with a private key
    std::string decrypt(std::string encryptedMessage, std::string sender, std::string privateKey) {
        // This is a placeholder function and should be replaced with actual decryption logic
        return "decrypted_message";
    }

    // Function to extract nonce from a decrypted message
    std::string extractNonce(std::string message) {
        // This is a placeholder function and should be replaced with actual extraction logic
        return "nonce_b";
    }

    // Function to extract identity from a decrypted message
    std::string extractIdentity(std::string message) {
        // This is a placeholder function and should be replaced with actual extraction logic
        return "bob";
    }
};

class Bob {
public:
    void receiveMessage(Message& message) {
        // Decrypt message from Alice
        std::string decryptedMessage = decrypt(message.contents, message.sender, myPrivateKey);

        // Extract nonce and identity from decrypted message
        std::string na = extractNonce(decryptedMessage);
        std::string aliceIdentity = extractIdentity(decryptedMessage);

        // Send back encrypted message with his nonce
        std::string encryptedResponse = encrypt(na, aliceIdentity, publicKey);
        std::cout << "Bob sends: " << encryptedResponse << std::endl;
    }

private:
    std::string myPrivateKey;
    std::string na;

    // Function to decrypt a message with a private key
    std::string decrypt(std::string encryptedMessage, std::string sender, std::string privateKey) {
        // This is a placeholder function and should be replaced with actual decryption logic
        return "decrypted_message";
    }

    // Function to encrypt a message with a public key
    std::string encrypt(std::string nonce, std::string receiver, std::string publicKey) {
        // This is a placeholder function and should be replaced with actual encryption logic
        return "encrypted_message";
    }

    // Function to extract nonce from a decrypted message
    std::string extractNonce(std::string message) {
        // This is a placeholder function and should be replaced with actual extraction logic
        return "nonce_b";
    }

    // Function to extract identity from a decrypted message
    std::string extractIdentity(std::string message) {
        // This is a placeholder function and should be replaced with actual extraction logic
        return "alice";
    }
};

int main() {
    // Create Alice's instance
    Alice alice;
    Message message;
    message.sender = "alice";
    message.receiver = "bob";

    // Initialize session
    alice.initiateSession(message);

    // Simulate Bob's response
    Message bobMessage;
    bobMessage.sender = "bob";
    bobMessage.receiver = "alice";
    alice.receiveMessage(bobMessage);

    return 0;
}
```
This code is a simplified implementation of the Needham-Schroeder protocol and includes placeholder functions for encryption, decryption, nonce extraction, and identity extraction. The `main` function initializes Alice's instance, simulates Bob's response, and demonstrates how the protocol works.

Please note that this is a very basic implementation and you should replace the placeholder functions with actual cryptographic functions to ensure secure communication.