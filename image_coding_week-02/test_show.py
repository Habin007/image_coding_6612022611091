import cv2 as cv
from pathlib import Path

# --- กำหนดค่าเริ่มต้น ---
# เปลี่ยนชื่อไฟล์ภาพนี้ให้ถูกต้อง หรือระบุพาธเต็ม
IMAGE_FILENAME = "test_image.jpg" 

def convert_and_show_separate(image_path: str):
    """
    อ่านภาพ, แปลงเป็นขาวดำ, และแสดงผลทั้งสองภาพในหน้าต่างแยกกันด้วย OpenCV.
    
    Args:
        image_path: เส้นทางไฟล์ไปยังภาพที่ต้องการประมวลผล.
    """
    
    # 1. การจัดการไฟล์และการตรวจสอบ
    p = Path(image_path)
    
    if not p.exists():
        print(f"❌ ข้อผิดพลาด: ไม่พบไฟล์ภาพที่ '{p.resolve()}'")
        return

    # 2. อ่านภาพด้วย OpenCV
    # cv.IMREAD_COLOR (1) โหลดภาพสี BGR
    img_bgr = cv.imread(str(p), cv.IMREAD_COLOR)

    if img_bgr is None:
        print(f"❌ ข้อผิดพลาด: ไม่สามารถโหลดภาพจาก '{p.resolve()}' ได้")
        return
        
    # 3. แปลงภาพเป็น Grayscale
    # cv.COLOR_BGR2GRAY จะแปลงภาพ BGR เป็น Grayscale
    img_grayscale = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
    
    # 4. แสดงผลภาพด้วย OpenCV ในหน้าต่างแยกกัน
    
    # แสดงภาพต้นฉบับ (Original Image)
    # OpenCV จะแสดงผลภาพในรูปแบบสี BGR ที่ถูกต้องในหน้าต่างนี้
    cv.imshow('1. Original Image (Color)', img_bgr)
    
    # แสดงภาพขาวดำ (Grayscale Image)
    cv.imshow('2. Grayscale Image', img_grayscale)
    
    # 5. รอให้ผู้ใช้กดปุ่มใดๆ เพื่อปิดหน้าต่าง
    print("\n✅ แสดงภาพเสร็จสมบูรณ์")
    print(">>> กรุณากดปุ่มใดๆ บนคีย์บอร์ดเพื่อปิดหน้าต่างแสดงผล...")
    
    cv.waitKey(0) # รอรับคีย์จากผู้ใช้ (0 คือรอตลอดไป)
    cv.destroyAllWindows() # ปิดหน้าต่าง OpenCV ทั้งหมด

# --- ฟังก์ชันหลักสำหรับการรันโค้ด ---
if __name__ == '__main__':
    current_dir = Path(__file__).parent
    full_image_path = current_dir / IMAGE_FILENAME
    
    convert_and_show_separate(str(full_image_path))
    print("✨ โปรแกรมจบการทำงาน")