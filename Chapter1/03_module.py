import flask
import pyjokes
# import django => Not installed (it's show an error)

print("Printing jokes...")

joke = pyjokes.get_joke()
print(joke)