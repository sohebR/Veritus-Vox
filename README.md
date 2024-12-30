# Veritus Vox 🛒🎙️  
**A Smart Grocery Management Assistant**  

**Veritus Vox** is an interactive Python-based mini-project that combines speech synthesis and a simple yet effective grocery management system. Designed for seamless user experience, it brings the power of voice-based interaction into a classic grocery billing system.

---

## Features 🌟  
### 🔊 **Voice-Integrated System**  
- Uses `pyttsx3` for text-to-speech capabilities, offering a voice assistant experience throughout the application.  

### ⏰ **Time-Based Greetings**  
- Welcomes users with contextual greetings based on the current time (morning, afternoon, evening).  

### 🛍️ **Dynamic Grocery Management**  
- A preloaded grocery list with prices.  
- Allows users to:  
  - Select items dynamically by name.  
  - Specify item quantities in appropriate units (e.g., liters, kilograms, packets, etc.).  
  - Generates an itemized bill with detailed breakdowns.

### 🧾 **Personalized Receipts**  
- Captures customer details like name and optional phone number.  
- Displays an itemized receipt with total cost calculations.  

### 💳 **Payment Validation**  
- Offers payment options for **cash** or **credit card**.  
- Implements **Luhn's Algorithm** to validate credit card numbers and identify card types (Visa, MasterCard, American Express).  

### 🎯 **User-Friendly Interaction**  
- Interactive prompts with real-time feedback, enabling an easy and intuitive user experience.  

---

## How It Works 🔍  
1. **Start the Program**: The program greets you and lists the available grocery items.  
2. **Add Items to Your Cart**: Select items by name, specify quantities, and the program computes costs dynamically.  
3. **Checkout**:  
   - Enter customer details.  
   - Choose a payment method (cash or card).  
   - If paying by card, the program validates the card details and identifies the card type.  
4. **Complete Your Purchase**: A final thank-you message is displayed along with the receipt.  

---

## Technologies Used 🛠️  
- **Python 3.x**  
- **Pyttsx3**: For speech synthesis.  
- **Datetime**: For dynamic greetings.  

---

## How to Run 🚀  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/Veritus-Vox.git  
   ```  
2. Install the required packages:  
   ```bash  
   pip install pyttsx3  
   ```  
3. Run the script:  
   ```bash  
   python veritus_vox.py  
   ```  

---

## Future Enhancements 🌱  
- Integrating speech-to-text for a fully voice-activated system.  
- Expanding the grocery list dynamically.  
- Adding support for multiple languages and regional pricing.  

---

## Contributing 🤝  
Contributions are welcome! Feel free to fork the repository, create issues, or submit pull requests to enhance this project.  

---

## License 📜  
This project is licensed under the MIT License. See the `LICENSE` file for more details.  
