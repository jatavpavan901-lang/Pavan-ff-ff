import time
import threading
import requests
from datetime import datetime
import os
from flask import Flask

app = Flask(__name__)

def keep_render_alive():

    RENDER_URL = "Your-Render-url"

    def ping_render():
        while True:
            try:
                # Wait 5 minutes (300 seconds)
                time.sleep(300)

                current_time = datetime.now().strftime("%H:%M:%S")

                try:
                    # Ping the Render URL
                    response = requests.get(f"{RENDER_URL}/", timeout=10)
                    print(f"[RENDER PING] ✅ Ping successful at {current_time} - Status: {response.status_code}")
                except Exception as e:
                    print(f"[RENDER PING] ❌ Failed at {current_time}: {e}")

            except Exception as e:
                print(f"[RENDER PING] ❌ Error in ping thread: {e}")
                time.sleep(60)

    ping_thread = threading.Thread(target=ping_render, daemon=True)
    ping_thread.start()
    print(f"[RENDER PING] 🚀 Auto-ping started: {RENDER_URL} (every 5 minutes)")


@app.route("/")
def home():
    return "Render server running ✅"


if __name__ == "__main__":
    keep_render_alive()  # ✅ Tumhara function call
    port = int(os.environ.get("PORT", 10000))  # ✅ Render dynamic port
    app.run(host="0.0.0.0", port=port)  # ✅ MUST for Render