import anthropic
import time
import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

class ClaudeArchitect:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-5-20250929" 

    def analyze_system(self, code_base: str, context_type: str):
        """
        Claude'un 1M token context window yeteneğini kullanarak geniş çaplı analiz yapar [cite: 9, 13]
        """
        print(f"\n[AGENTIC REASONING] Analyzing {context_type} for architectural bottlenecks...")
        
        system_prompt = (
            "You are a Senior Software Architect. Your task is to perform an 'Intelligent CI/CD Review'. "
            "Focus on scalability, infrastructure reliability, and security compliance (GDPR/KVKK)."
        )

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                temperature=0, 
                system=system_prompt,
                messages=[
                    {"role": "user", "content": f"Review this for {context_type} issues:\n\n{code_base}"}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"API Connection Error: {str(e)}"

# --- DEMO SCRIPTS ---

def run_comprehensive_demo(api_key):
    architect = ClaudeArchitect(api_key)
    
    # Senaryo 1: Veritabanı ve Ölçeklenebilirlik (N+1 Problemi) [cite: 43]
    performance_code = """
    def fetch_user_data(user_ids):
        for uid in user_ids:
            # Potansiyel performans darboğazı
            data = db.execute(f"SELECT * FROM profiles WHERE user_id = {uid}")
            process(data)
    """
    
    # Senaryo 2: Mikroservis Altyapısı (Shared Database Risk) [cite: 44]
    infra_config = """
    infrastructure_map:
      order_service: connects_to(primary_db)
      payment_service: connects_to(primary_db)
      inventory_service: connects_to(primary_db)
    """

    print("--- STARTING ARCHITECTURAL AUDIT ---")
    
    # 1. Analiz
    perf_report = architect.analyze_system(performance_code, "Scalability & N+1 Patterns")
    print(f"REPORT 1:\n{perf_report}\n")

    # 2. Analiz
    infra_report = architect.analyze_system(infra_config, "Microservices Isolation (SPOF)")
    print(f"REPORT 2:\n{infra_report}\n")

if __name__ == "__main__":
    MY_KEY = os.environ.get("ANTHROPIC_API_KEY")
    run_comprehensive_demo(MY_KEY)