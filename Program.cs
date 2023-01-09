// See https://aka.ms/new-console-template for more information

using HumanReadableTimeExercise;

const int MAX_SEC = 359999;
const int sec1 = MAX_SEC;
const int sec2 = 0;
const int sec3 = 2;
const int sec4 = 7777;

Console.WriteLine(HumanReadableTime.GetReadableTime(sec1));
Console.WriteLine(HumanReadableTime.GetReadableTime(sec2));
Console.WriteLine(HumanReadableTime.GetReadableTime(sec3));
Console.WriteLine(HumanReadableTime.GetReadableTime(sec4));
