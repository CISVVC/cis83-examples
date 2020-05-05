#include<iostream>

int main()
{
   int num1,num2;
   std::cout << "Enter the first number: ";
   std::cin >> num1;
   std::cout << "Enter the second number: ";
   std::cin >> num2;
   std::cout << num1 << " + " << num2 << " = " << (num1+num2) << std::endl;
   return 0;
}
