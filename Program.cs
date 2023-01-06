// See https://aka.ms/new-console-template for more information

using SplitStringsExercise;

string s1 = "abc";
string s2 = "abcdef";

Console.WriteLine(string.Join(", ", SplitStrings.Solution(s1)));
Console.WriteLine(string.Join(", ", SplitStrings.Solution(s2)));
