import os
import json
from openai import OpenAI

# 1. Konfigurasi Client DeepSeek
# Pastikan Environment Variable DEEPSEEK_API_KEY sudah terpasang
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"), 
    base_url="https://api.deepseek.com"
)

# ==========================================
# SKILLS PROSEDURAL (TOOLS)
# ==========================================

def check_inventory(product_name: str):
    """Mengecek ketersediaan stok barang di gudang."""
    print(f"\n[Skill] Memeriksa stok untuk: {product_name}")
    inventory = {
        "laptop": 5,
        "mouse": 0,
        "keyboard": 12
    }
    stock = inventory.get(product_name.lower(), 0)
    return json.dumps({"product": product_name, "stock": stock})

def calculate_discount(price: float, member_level: str):
    """Menghitung harga akhir berdasarkan level keanggotaan."""
    print(f"\n[Skill] Menghitung diskon untuk level: {member_level}")
    discount = 0
    if member_level.lower() == "gold":
        discount = 0.20 
    elif member_level.lower() == "silver":
        discount = 0.10 
    
    final_price = price * (1 - discount)
    return json.dumps({"original_price": price, "discount": discount, "final_price": final_price})

def send_confirmation(email: str, message: str):
    """Mengirim email konfirmasi transaksi."""
    print(f"\n[Skill] Mengirim email ke: {email}")
    return json.dumps({"status": "success", "to": email})

tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "check_inventory",
            "description": "Cek stok barang di gudang",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"}
                },
                "required": ["product_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_discount",
            "description": "Hitung diskon member",
            "parameters": {
                "type": "object",
                "properties": {
                    "price": {"type": "number"},
                    "member_level": {"type": "string", "enum": ["gold", "silver", "regular"]}
                },
                "required": ["price", "member_level"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_confirmation",
            "description": "Kirim email konfirmasi",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "message": {"type": "string"}
                },
                "required": ["email", "message"]
            }
        }
    }
]

# ==========================================
# AI AGENT CLASS
# ==========================================

class SkillsAgent:
    def __init__(self, model="deepseek-chat"):
        self.model = model
        self.messages = [
            {"role": "system", "content": (
                "Anda adalah Prosedural AI Agent. "
                "Ikuti prosedur: 1.Cek stok, 2.Hitung diskon jika ada, 3.Kirim email jika deal."
            )}
        ]

    def execute(self, prompt: str):
        self.messages.append({"role": "user", "content": prompt})
        
        while True:
            response = client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=tools_schema
            )

            msg = response.choices[0].message
            self.messages.append(msg)

            if not msg.tool_calls:
                break

            for tool_call in msg.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                
                if name == "check_inventory":
                    res = check_inventory(**args)
                elif name == "calculate_discount":
                    res = calculate_discount(**args)
                elif name == "send_confirmation":
                    res = send_confirmation(**args)
                else:
                    res = "Unknown tool"

                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": res
                })

        return msg.content

if __name__ == "__main__":
    agent = SkillsAgent()
    print("--- Prosedural AI Agent Ready ---")
    user_input = "Saya ingin beli Laptop, saya member Silver. Email saya budi@mail.com"
    print(f"User: {user_input}")
    print(f"Agent: {agent.execute(user_input)}")
