import torch

isUseable = torch.cuda.is_available()

print(f"GPU 사용 가능 여부 : {isUseable}")

if isUseable:

    print(f"GPU수 : {torch.cuda.device_count()}")

    print(f"GPU명 : {torch.cuda.get_device_name(0)}")