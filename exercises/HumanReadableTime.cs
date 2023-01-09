namespace HumanReadableTimeExercise;

public static class HumanReadableTime
{
    private static readonly int SEC_IN_MIN = 60;
    private static readonly int SEC_IN_HR = 3600;

    public static string GetReadableTime(int seconds)
    {
        int hours = seconds / SEC_IN_HR;
        seconds -= hours * SEC_IN_HR;
        int minutes = seconds / SEC_IN_MIN;
        seconds -= minutes * SEC_IN_MIN;
        return $"{hours:D2}:{minutes:D2}:{seconds:D2}";
    }
}
