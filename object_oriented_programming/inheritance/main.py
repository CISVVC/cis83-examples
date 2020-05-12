int main()
{
   vector<Employee*> staff;
   staff.push_back(new HourlyEmployee("Morgan, Harry", 30));
   staff.push_back(new SalariedEmployee("Lin, Sally", 52000)); 
   staff.push_back(new Manager("Smith, Mary", 104000, 50));
      
   for (int i = 0; i < staff.size(); i++)
   {
      cout << "Hours worked by " << staff[i]->get_name() << ": ";
      int hours;
      cin >> hours;
      cout << "Salary: " << staff[i]->weekly_pay(hours) << endl;
   }

   return 0;
}
