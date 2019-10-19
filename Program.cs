using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using LumenWorks.Framework.IO.Csv;
using System.Data;

namespace NormallyDistributedRandomNumberGenerator
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            var list = new List<double>();
            int mean = 500000;
            int stdDev = 100000;
            var csv = new StringBuilder();
            for (var i = 0; i < 1000000; i++)
            {
                double u1 = 1.0 - rand.NextDouble();
                double u2 = 1.0 - rand.NextDouble();
                double randStdNormal = Math.Sqrt(-2.0 * Math.Log(u1)) * Math.Sin(2.0 * Math.PI * u2);
                double randNormal = mean + stdDev * randStdNormal;
                csv.Append($"{Math.Round(randNormal)}\r\n");
            }
            File.WriteAllText("Your path here", csv.ToString());
        }
    }
}
