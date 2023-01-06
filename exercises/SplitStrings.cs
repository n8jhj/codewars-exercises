namespace SplitStringsExercise;

public static class SplitStrings
{
    public static string[] Solution(string str)
    {
        if (str.Length % 2 != 0)
        {
            str += "_";
        }

        var pieces = new List<string>();
        for (int i = 0; i < str.Length; i += 2)
        {
            pieces.Add(str[i].ToString() + str[i + 1]);
        }
        return pieces.ToArray();
    }
}
