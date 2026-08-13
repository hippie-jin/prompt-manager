def create_default_prompts():
    return [
        {
            "title": "블로그 글 작성 도우미",
            "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
            "category": "텍스트 생성",
            "favorite": False,
        },
        {
            "title": "유튜브 썸네일 이미지 생성",
            "content": "다음 영상 주제에 어울리는 유튜브 썸네일 이미지를 생성해주세요. 밝고 눈에 띄는 색감, 큰 텍스트, 클릭을 유도하는 표정과 구도를 포함해주세요. 주제: {영상 주제}",
            "category": "이미지 생성",
            "favorite": False,
        },
        {
            "title": "시니어 백엔드 개발자 페르소나",
            "content": "당신은 10년차 시니어 백엔드 개발자입니다. 신입 개발자의 질문에 대해 원리를 쉽게 풀어서 설명하고, 실무에서 자주 하는 실수와 그 이유까지 함께 알려주세요.",
            "category": "페르소나",
            "favorite": False,
        },
        {
            "title": "일일 이메일 요약 자동화",
            "content": "받은 이메일 목록을 입력하면, 각 메일을 한 줄로 요약하고 긴급도(높음/보통/낮음)를 표시해주세요. 마지막에 오늘 처리해야 할 우선순위 3가지를 정리해주세요.",
            "category": "자동화",
            "favorite": False,
        },
    ]

def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ")
    while title.strip() == "":
        print("제목을 입력해주세요.")
        title = input("제목: ")

    content = input("내용: ")
    while content.strip() == "":
        print("내용을 입력해주세요.")
        content = input("내용: ")

    print("\n카테고리 선택:")
    print("1) 텍스트 생성")
    print("2) 이미지 생성")
    print("3) 영상 생성")
    print("4) 페르소나")
    print("5) 자동화")
    print("6) 기타")
    print("7) 직접 입력")

    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    category_choice = input("선택: ")

    if category_choice in ["1", "2", "3", "4", "5", "6"]:
        category = categories[int(category_choice) - 1]
    else:
        category = input("카테고리 직접 입력: ")

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })

    print("\n프롬프트가 추가되었습니다!")

def list_prompts(prompts):
    print("\n=== 프롬프트 목록 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = "★" if prompt["favorite"] else " "
        print(f"{index}. [{star}] {prompt['title']} ({prompt['category']})")

def view_by_category(prompts):
    print("\n=== 카테고리별 조회 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    categories = sorted(set(prompt["category"] for prompt in prompts))

    print("\n카테고리 목록:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    choice = input("카테고리 선택: ")
    while not choice.isdigit() or not (1 <= int(choice) <= len(categories)):
        print("올바른 번호를 입력해주세요.")
        choice = input("카테고리 선택: ")

    selected_category = categories[int(choice) - 1]
    filtered = [prompt for prompt in prompts if prompt["category"] == selected_category]

    print(f"\n=== {selected_category} ({len(filtered)}개) ===")
    for index, prompt in enumerate(filtered, start=1):
        star = "★" if prompt["favorite"] else " "
        print(f"{index}. [{star}] {prompt['title']}")

def search_prompts(prompts):
    print("\n=== 프롬프트 검색 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input("검색어: ")
    while keyword.strip() == "":
        print("검색어를 입력해주세요.")
        keyword = input("검색어: ")

    results = [
        prompt for prompt in prompts
        if keyword.lower() in prompt["title"].lower() or keyword.lower() in prompt["content"].lower()
    ]

    if len(results) == 0:
        print(f"\n'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print(f"\n=== 검색 결과 ({len(results)}개) ===")
    for index, prompt in enumerate(results, start=1):
        star = "★" if prompt["favorite"] else " "
        print(f"{index}. [{star}] {prompt['title']} ({prompt['category']})")

def show_prompt_detail(prompts):
    print("\n=== 프롬프트 상세 보기 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = "★" if prompt["favorite"] else " "
        print(f"{index}. [{star}] {prompt['title']} ({prompt['category']})")

    choice = input("번호 선택: ")
    while not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("올바른 번호를 입력해주세요.")
        choice = input("번호 선택: ")

    prompt = prompts[int(choice) - 1]
    print(f"\n제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
    print(f"내용:\n{prompt['content']}")

def manage_favorites(prompts):
    print("\n=== 즐겨찾기 관리 ===")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = "★" if prompt["favorite"] else " "
        print(f"{index}. [{star}] {prompt['title']} ({prompt['category']})")

    choice = input("즐겨찾기 설정/해제할 번호: ")
    while not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("올바른 번호를 입력해주세요.")
        choice = input("즐겨찾기 설정/해제할 번호: ")

    prompt = prompts[int(choice) - 1]
    prompt["favorite"] = not prompt["favorite"]
    status = "즐겨찾기에 추가되었습니다." if prompt["favorite"] else "즐겨찾기에서 해제되었습니다."
    print(f"\n'{prompt['title']}' {status}")

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
    prompts = create_default_prompts()
    while True:
        show_menu()
        choice = input("선택: ")
        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            list_prompts(prompts)
        elif choice == "3":
            view_by_category(prompts)
        elif choice == "4":
            search_prompts(prompts)
        elif choice == "5":
            show_prompt_detail(prompts)
        elif choice == "6":
            manage_favorites(prompts)
        elif choice == "7":
            print("(준비 중) 즐겨찾기 목록")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")

main()