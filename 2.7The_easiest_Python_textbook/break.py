while True:
    command = input("pybot> ")
    if "こんにちは" in command:
        print("こんにちは！")
    elif "ありがとう" in command:
        print("どういたしまして！")
    elif "さようなら" in command:
        print("さようなら！またね！")
    elif "お疲れ様でした" in command:
        print("お疲れ様です！")
        break
    else:
        print("気安く話しかけるな！")
        break
