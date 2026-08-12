def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def main():
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "1":
            print("(준비 중) 프롬프트 추가")
        elif choice == "2":
            print("(준비 중) 프롬프트 목록")
        elif choice == "3":
            print("(준비 중) 카테고리별 조회")
        elif choice == "4":
            print("(준비 중) 프롬프트 검색")
        elif choice == "5":
            print("(준비 중) 프롬프트 상세 보기")
        elif choice == "6":
            print("(준비 중) 즐겨찾기 관리")
        elif choice == "7":
            print("(준비 중) 즐겨찾기 목록")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")

main()