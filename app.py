from configparser import ConfigParser
import google.generativeai as genai

# 讀取 API 金鑰
config = ConfigParser()
config.read("config.ini")
api_key = config["Gemini"]["API_KEY"]

# 設定 Gemini 模型
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# 提問範例
def generate_health_advice(user_input):
    prompt = f"""
你是一位專門照顧老年人身心健康的照護顧問。
請根據以下使用者的描述，判斷：

1. 是否需要就醫，若需要，請說明理由並建議前往哪一類的醫療科別。
2. 若不需立即就醫，請給出簡單易行的生活建議（心理與身體面向皆可），不須用太多字給予重點即可。
3. 語氣請溫和友善，內容適合60歲以上長者閱讀。

使用者描述如下：
"{user_input}"
    """

    response = model.generate_content(prompt)
    return response.text

#最近晚上常常失眠，心情也有點低落，吃東西也沒什麼胃口。
#我最近胸口常常悶悶的，有時會突然感覺呼吸困難，連走幾步路都覺得很累。昨天晚上還有點冒冷汗。

# 使用範例
if __name__ == "__main__":
    user_input = input("請描述您的身體或心理狀況：")
    advice = generate_health_advice(user_input)
    print("\nAI 健康建議：\n")
    print(advice)
