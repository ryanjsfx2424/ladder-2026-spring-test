# **🌊 VIBE CODING MANIFEST: WEB APP EVOLUTION**

## **0\. THE PRIME DIRECTIVE**

Maintain the "Flow State" at all costs. Code is secondary to the vibe. The AI must act as an intuitive extension of the developer's intent, prioritizing speed, modern aesthetics, and the specific technical stack defined below.

## **1\. TECHNICAL STACK & CONSTRAINTS**

### **🚫 FORBIDDEN LIBRARIES**

* **DO NOT USE** google-generativeai. This is considered legacy for this project.  
* **DO NOT USE** langchain or complex wrappers unless explicitly requested.

### **✅ MANDATORY SDK**

* **ALWAYS USE** the modern google-genai SDK.  
* **IMPORT PATTERN (Python):** from google import genai  
* **IMPORT PATTERN (JS):** import { createClient } from "@google/generative-ai" (Ensure usage of the latest unified client logic).

### **🤖 MODEL LOCK**

* **PRIMARY MODEL:** gemini-2.5-flash-lite  
* **REASONING:** High-speed tokens, low latency, and optimized for the iterative "vibe" loop.  
* **INSTRUCTION:** Never default to gemini-pro or older 1.5 versions unless the Lite model physically cannot handle the context window.

## **2\. CODING STANDARDS (THE VIBE)**

### **A. UI/UX Philosophy**

* **Modern Defaults:** Use Tailwind CSS for everything. Rounded corners (rounded-xl), subtle shadows (shadow-sm), and plenty of whitespace.  
* **Glassmorphism:** When in doubt, add a backdrop blur.  
* **Motion:** Use Framer Motion (React) or simple CSS transitions for state changes.

### **B. Implementation Logic**

* **Single-File Preference:** For prototypes, keep logic, styles, and components in one clean file until it "breaks the vibe" (becomes unreadable).  
* **Functional over Class:** Always prefer functional components and hooks.  
* **Modern ESM:** Use import/export syntax exclusively.

## **3\. BOT OPERATIONAL PROTOCOL**

### **Initialization Template (Python)**

from google import genai

\# Setup for gemini-2.5-flash-lite  
client \= genai.Client(api\_key="YOUR\_API\_KEY")

def generate\_vibe(prompt):  
    response \= client.models.generate\_content(  
        model="gemini-2.5-flash-lite",  
        contents=prompt  
    )  
    return response.text

### **Response Style**

1. **Brief & Punchy:** Minimize "As an AI language model" fluff.  
2. **Code-First:** Provide the solution first, explanation second.  
3. **Vibe Check:** If a request ruins the app's aesthetic or performance, suggest a "cooler" way to do it.

## **4\. PROJECT EVOLUTION**

1. **Vibe 1: Sketching** (Raw HTML/JS/CSS prototypes).  
2. **Vibe 2: Structure** (Componentization and State Management).  
3. **Vibe 3: Intelligence** (Integrating google-genai features).  
4. **Vibe 4: Polish** (Micro-interactions and deployment).

**Status:** Ready to Build.

**Model Active:** gemini-2.5-flash-lite

**SDK Status:** google-genai logic loaded.