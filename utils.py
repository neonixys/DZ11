# Импортируем json
import json


def load_candidates_from_json():
    """Функция возвращает список всех кандидатов"""
    with open("candidates.json", 'r', encoding="UTF-8") as file:
        return json.load(file)


def get_candidate(id: int):
    """Функция возвращает одного кандидата по его id"""
    for i in load_candidates_from_json():
        if i['id'] == id:
            return i


def get_candidates_by_name(candidate_name: str):
    """Функция возвращает кандидатов по имени"""
    candidates = []
    for i in load_candidates_from_json():
        if candidate_name.lower() in i['name'].lower():
            candidates.append(i)
    return candidates


def get_candidates_by_skill(skill_name: str):
    """Функция возвращает кандидатов по навыку"""
    skills = []
    for i in load_candidates_from_json():
        if skill_name.lower() in i['skills'].lower().split(', '):
            skills.append(i)
    return skills
