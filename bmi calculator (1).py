def calculate_bmi(weight, height):
  bmi = weight / (height ** 2)
  return bmi

def interpret_bmi(bmi):
  if bmi < 18.5:
      return "Underweight"
  elif 18.5 <= bmi < 24.9:
      return "Normal weight"
  elif 25 <= bmi < 29.9:
      return "Overweight"
  else:
      return "Obese"

def main():
  print("----BMI Calculator-----")
  name=input("Enter Your Name:")
  print("Hello",name,"!")
  print("---Welcome to BMI Calculator---")
  print("Choose your desired option")
  print("1. Calculate BMI")
  print("2. Check BMI category")
  print("3. Exit")

  option = input("Choose an option (1, 2, or 3): ")

  if option == "1":
      # Get user input for weight and height
      weight = float(input("Enter your weight in kilograms: "))
      height = float(input("Enter your height in meters: "))

      # Calculate BMI
      bmi = calculate_bmi(weight, height)

      # Interpret BMI
      interpretation = interpret_bmi(bmi)

      # Display the result
      print(f"Your BMI is: {bmi:.2f}")
      print(f"You are classified as: {interpretation}")
  elif option == "2":
      # Get user input for current BMI
      current_bmi = float(input("Enter your current BMI: "))

      # Interpret BMI
      interpretation = interpret_bmi(current_bmi)

      # Display the result
      print(f"Your current BMI is: {current_bmi:.2f}")
      print(f"You are currently classified as: {interpretation}")
  elif option == "3":
      print("Exiting the BMI Calculator.")
  else:
      print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
  main()

