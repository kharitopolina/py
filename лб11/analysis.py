def validate_todos(data):
    if type(data) is not list:
        raise ValueError("Корневой элемент JSON должен быть списком")
    seen_ids = set()
    for item in data:
        if type(item) is not dict:
            raise ValueError("Каждый элемент списка задач должен быть словарём")
        for required_key in ("id", "userId", "title", "completed"):
            if required_key not in item:
                raise ValueError(f"Отсутствует обязательное поле '{required_key}'")
        task_id = item["id"]
        if type(task_id) is not int or task_id <= 0:
            raise ValueError("Поле 'id' должно быть положительным целым числом")
        if task_id in seen_ids:
            raise ValueError(f"Обнаружен повторяющийся 'id': {task_id}")
        seen_ids.add(task_id)
        user_id = item["userId"]
        if type(user_id) is not int or user_id <= 0:
            raise ValueError("Поле 'userId' должно быть положительным целым числом")
        title = item["title"]
        if type(title) is not str or not title.strip():
            raise ValueError("Поле 'title' должно быть непустой строкой")
        completed = item["completed"]
        if type(completed) is not bool:
            raise ValueError("Поле 'completed' должно быть логическим значением (bool)")
def completion_counts(todos):
    counts = {}
    for task in todos:
        user_id = task["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if task["completed"] is True:
            counts[user_id] += 1
    return counts
def top_users(counts):
    if not counts:
        return []
    max_done = max(counts.values())
    if max_done <= 0:
        return []
    leaders = [user_id for user_id, done in counts.items() if done == max_done]
    leaders.sort()
    return leaders
def get_leader_completed_tasks(todos, leaders):
    leader_set = set(leaders)
    result = []
    for task in todos:
        if task["userId"] in leader_set and task["completed"] is True:
            result.append(task)
    return result
def select_tasks(todos, user_id, parameter=None):
    selected = []
    for task in todos:
        if task["userId"] == user_id and task["id"] % 2 == 0:
            selected.append(task)
    return selected
