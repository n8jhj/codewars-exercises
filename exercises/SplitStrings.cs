namespace SplitStringsExercise;

public class SplitStrings
{
    public static string[] Solution(string str)
    {
        var pieces = new string[(str.Length + 1) / 2];
        string piece = "";
        int count = 0;
        foreach (char c in str)
        {
            if (piece.Length < 2)
            {
                piece += c;
            }
            else
            {
                pieces[count] = piece;
                count++;
                piece = c.ToString();
            }
        }
        if (piece.Length < 2)
        {
            piece += '_';
        }
        pieces[count] = piece;
        return pieces;
    }
}
