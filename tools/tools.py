from datetime import datetime
from typing import Dict, List, Optional

class CourseInfoTool:
    def __init__(self):
        
        self.courses = {
            "cucina_base": {
                "name": "Cucina Base",
                "description": "Corso base di cucina tradizionale italiana",
                "duration": "4 settimane",
                "price": 299.99
            },
            "pasticceria": {
                "name": "Pasticceria Professionale",
                "description": "Tecniche avanzate di pasticceria e dessert",
                "duration": "6 settimane",
                "price": 399.99
            },
            "cucina_mediterranea": {
                "name": "Cucina Mediterranea",
                "description": "Piatti tipici della tradizione mediterranea",
                "duration": "5 settimane",
                "price": 349.99
            },
            "pizza_master": {
                "name": "Master Pizzaiolo",
                "description": "Tecniche professionali per la preparazione della pizza",
                "duration": "3 settimane",
                "price": 279.99
            },
            "bbq_master": {
                "name": "BBQ Master",
                "description": "Arte della cucina Carnivore e tecniche innovative",
                "duration": "4 settimane",
                "price": 329.99
            }
        }

    def get_info(self, course_name: str) -> str:
        course = self.courses.get(course_name.lower().replace(" ", "_"))
        if not course:
            context = self.courses
            return f"Corso non trovato con tale nome. ecco i corsi disponibili: {context}"
        return (f"Corso: {course['name']}\n"
                f"Descrizione: {course['description']}\n"
                f"Durata: {course['duration']}\n"
                f"Prezzo: €{course['price']}")


class ScheduleTool:
    def __init__(self):
        
        self.classes = [
            {
                "course_name": "Cucina Base",
                "start_date": "2025-06-15",
                "end_date": "2025-07-15",
                "spots_available": 12
            },
            {
                "course_name": "Pasticceria Professionale",
                "start_date": "2025-06-01",
                "end_date": "2025-07-15",
                "spots_available": 8
            },
            {
                "course_name": "Cucina Mediterranea",
                "start_date": "2025-06-20",
                "end_date": "2025-07-25",
                "spots_available": 10
            },
            {
                "course_name": "Master Pizzaiolo",
                "start_date": "2025-06-01",
                "end_date": "2025-07-21",
                "spots_available": 6
            },
            {
                "course_name": "BBQ Master",
                "start_date": "2025-08-15",
                "end_date": "2025-09-15",
                "spots_available": 15
            }
        ]

    def get_classes(self, course_name: Optional[str] = None, 
                         start_date: Optional[str] = None) -> str:
        filtered_classes = self.classes
        if course_name:
            filtered_classes = [c for c in filtered_classes 
                              if c["course_name"].lower() == course_name.lower()]
        if start_date:
            filtered_classes = [c for c in filtered_classes 
                              if c["start_date"] >= start_date]
        
        if not filtered_classes:
            return f"Nessuna classe trovata per i criteri specificati. Ecco le classi in partenza: {self.classes}"
        
        result = "Prossime classi disponibili:\n"
        for c in filtered_classes:
            result += (f"- {c['course_name']}: {c['start_date']} - {c['end_date']}, "
                      f"Posti disponibili: {c['spots_available']}\n")
        return result

class BookingTool:
    def __init__(self):
       
        self.available_slots = [
            {
                "teacher_id": "T001",
                "teacher_name": "Prof. Rossi",
                "date": "2025-05-25",
                "time": "14:00"
            },
            {
                "teacher_id": "T002",
                "teacher_name": "Prof. Bianchi",
                "date": "2025-05-28",
                "time": "15:30"
            },
            {
                "teacher_id": "T003",
                "teacher_name": "Prof. Verdi",
                "date": "2025-05-30",
                "time": "16:30"
            },
            {
                "teacher_id": "T004",
                "teacher_name": "Prof. Neri",
                "date": "2025-06-01",
                "time": "10:00"
            },
            {
                "teacher_id": "T005",
                "teacher_name": "Prof. Gialli",
                "date": "2025-06-01",
                "time": "10:00"
            },
            {
                "teacher_id": "T006",
                "teacher_name": "Prof. Marroni",
                "date": "2025-06-02",
                "time": "09:30"
            },
            {
                "teacher_id": "T007",
                "teacher_name": "Prof. Viola",
                "date": "2025-06-05",
                "time": "11:00"
            },
            {
                "teacher_id": "T008",
                "teacher_name": "Prof. Rosa",
                "date": "2025-06-10",
                "time": "14:30"
            },
            {
                "teacher_id": "T009",
                "teacher_name": "Prof. Celeste",
                "date": "2025-06-15",
                "time": "16:00"
            },
            {
                "teacher_id": "T010",
                "teacher_name": "Prof. Arancione",
                "date": "2025-06-20",
                "time": "10:30"
            },
            {
                "teacher_id": "T011",
                "teacher_name": "Prof. Azzurro",
                "date": "2025-07-01",
                "time": "15:00"
            },
            {
                "teacher_id": "T012",
                "teacher_name": "Prof. Verde",
                "date": "2025-07-10",
                "time": "17:30"
            },
            {
                "teacher_id": "T013",
                "teacher_name": "Prof. Blu",
                "date": "2025-07-20",
                "time": "09:30"
            },
            {
                "teacher_id": "T014",
                "teacher_name": "Prof. Grigio",
                "date": "2025-07-25",
                "time": "13:00"
            },
            {
                "teacher_id": "T015",
                "teacher_name": "Prof. Beige",
                "date": "2025-08-01",
                "time": "11:30"
            },
            {
                "teacher_id": "T016",
                "teacher_name": "Prof. Oro",
                "date": "2025-08-05",
                "time": "14:00"
            },
            {
                "teacher_id": "T017",
                "teacher_name": "Prof. Argento",
                "date": "2025-08-10",
                "time": "16:30"
            },
            {
                "teacher_id": "T018",
                "teacher_name": "Prof. Bronzo",
                "date": "2025-08-15",
                "time": "10:00"
            },
            {
                "teacher_id": "T019",
                "teacher_name": "Prof. Rame",
                "date": "2025-08-20",
                "time": "15:30"
            },
            {
                "teacher_id": "T020",
                "teacher_name": "Prof. Platino",
                "date": "2025-08-25",
                "time": "17:00"
            },
        ]

    def book_consultation(self, date: str, time: str, 
                              teacher_id: Optional[str] = None) -> str:
        available = [slot for slot in self.available_slots 
                    if slot["date"] == date and slot["time"] == time]
        
        if teacher_id:
            available = [slot for slot in available 
                        if slot["teacher_id"] == teacher_id]
        
        if not available:
            disp = self.available_slots
            return (f"Mi dispiace, nessuna disponibilità trovata per la data e l'ora specificate. Ecco tutte le disponibilita' al momento {disp}")
      
        slot = available[0]
        return (f"Prenotazione confermata con {slot['teacher_name']} "
                f"per il {slot['date']} alle {slot['time']}")
