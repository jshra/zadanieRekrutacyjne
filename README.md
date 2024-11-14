HTML Generator

Prosta aplikacja w języku Python pozwalająca generowanie sformatowanego kodu HTML przy użyciu API OpenAi

Wymagania:
-Python 3.x
-Zainstalowana biblioteka OpenAI
-Klucz API OpenAi

Działanie:
1. Aplikacja łączy się z API OpenAi
2. Odczytuje plik tekstowy zawierający treść artykułu 
3. Przekazuje treść artykułu z odpowiednim promptem do modelu gpt-4o
4. Otrzymany kod HTML zapisuje w pliku
5. Dodatkowo generuje przykładowy widok strony na podstawie pliku z szablonem

Struktura plików:
-'text.txt' - plik z artykułem tekstowym 
-'szablon.html' - szablon HTML do generowania podglądu
-'artykul.html' - plik z wygenerowanym kodem HTML
-'podgląd.html' - przykładowy widok strony utworzony na podstawie wygenerowanego kodu i szablonu

 Uruchomienie:
1. Instalacja potrzebnych bibliotek
2. Przygotowanie plików 'text.txt' z treścią artykułu i 'szablon.html' z szablonem HTML do wyświetlenia artykułu
3. Uruchomienie aplikacji (np. przy pomocy komendy >python htmlGenerator.py lub wewnątrz IDE)
 
