using System;
using System.IO;
using System.Collections.Generic;

namespace Boggle
{
    public interface IResults
    {
        IEnumerable<string> Words { get; } // unique found words
        int Score { get; }                 // total score for all words found
    }
    public interface ISolver
    {
        // board: 'q' represents the 'qu' Boggle cube
        IResults FindWords(char[,] board);
    }
    public class ResultsTable : IResults
    {
        public static List<string> Words1 = new List<string>(); // List of words

        public IEnumerable<string> Words
        {
            get
            {
                return Words1;
            }
        }
        public int Score
        {
            get
            {
                return Words1.Count;        // Return count of words
            }
        }
    }

    public class MyBoggleSolution
    {
        public static ISolver CreateSolver(string dictionaryPath)
        {
            return new Boggle(dictionaryPath);
        }
    }
    public class Boggle : ISolver
    {
        public static readonly int ALPHA_LENGTH = 26;   // Alphabet size in English
        public static readonly int M = 3;       // To change the size of the board...
        public static readonly int N = 3;       // change the dimensions here and change the board too
        public TrieNode root;

        public Boggle(string s)
        {
            List<String> dictionary = new List<string>();   // Dictionary as ArrayList
            using (StreamReader sr = new StreamReader(s))
            {
                try
                {
                    string line;
                    while ((line = sr.ReadLine()) != null)  // Read the Dictionary text file and store in ArrayList
                    {
                        dictionary.Add(line);
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine("The file could not be read:");
                    Console.WriteLine(ex.Message);
                }
                sr.Close();
            }
            // Root as new TrieNode 
            root = new TrieNode();

            // Insert all words from dictionary into the root node 
            int n = dictionary.Count;
            for (int i = 0; i < n; i++)
            {
                Insert(root, dictionary[i]);
            }
            // You can define your own board here
            char[,] board = {{'d','z','x'},
                            {'e','a','i'},
                            {'q','u','t'}
            };
            FindWords(board);
        }

        // Trie
        public class TrieNode
        {
            public TrieNode[] Child = new TrieNode[ALPHA_LENGTH];   // of length 26
            public bool isLeaf; // boolean to check if is leaf or not
            
            public TrieNode()
            {
                isLeaf = false;
                for (int i = 0; i < ALPHA_LENGTH; i++)
                {
                    Child[i] = null;
                }
            }
        }
 
        // If the key is prefix of trie, it marks leaf node 
        static void Insert(TrieNode root, String Key)
        {
            int n = Key.Length;
            TrieNode p = root;
            for (int i = 0; i < n; i++)
            {
                int index = Key[i] - 'a'; // To normalize

                if (p.Child[index] == null)
                {
                    p.Child[index] = new TrieNode();
                }
                p = p.Child[index];
            } 
            p.isLeaf = true;
        }

        // Method to print present words using recursion 
        static void SearchWord(TrieNode root, char[,] boggle, int i, int j, bool[,] visitTable, String str)
        {
            // If word is found
            if (root.isLeaf == true)
            {
                Console.WriteLine(str);
                ResultsTable.Words1.Add(str);
            }

            // If i,j in range and we have already visited the element 
            if (IsSafe(i, j, visitTable))
            {
                visitTable[i, j] = true;

                // Traverse children
                for (int K = 0; K < ALPHA_LENGTH; K++)
                {
                    if (root.Child[K] != null)
                    {
                        // Current char
                        char ch = (char)(K + 'a'); // De-normalize

                        // Recursively search for remaining characters in all 8 adjacent cells
                        if (IsSafe(i - 1, j - 1, visitTable) && boggle[i - 1, j - 1] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i - 1, j - 1, visitTable, str + ch);
                        }
                        if (IsSafe(i - 1, j, visitTable) && boggle[i - 1, j] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i - 1, j, visitTable, str + ch);
                        }
                        if (IsSafe(i + 1, j - 1, visitTable) && boggle[i + 1, j - 1] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i + 1, j - 1, visitTable, str + ch);
                        }
                        if (IsSafe(i, j - 1, visitTable) && boggle[i, j - 1] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i, j - 1, visitTable, str + ch);
                        }
                        if (IsSafe(i - 1, j + 1, visitTable) && boggle[i - 1, j + 1] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i - 1, j + 1, visitTable, str + ch);
                        }
                        if (IsSafe(i + 1, j, visitTable) && boggle[i + 1, j] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i + 1, j, visitTable, str + ch);
                        }
                        if (IsSafe(i + 1, j + 1, visitTable) && boggle[i + 1, j + 1] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i + 1, j + 1, visitTable, str + ch);
                        }
                        if (IsSafe(i, j + 1, visitTable) && boggle[i, j + 1] == ch)
                        {
                            SearchWord(root.Child[K], boggle, i, j + 1, visitTable, str + ch);
                        }
                    }
                }

                // Current element unvisited 
                visitTable[i, j] = false;
            }
        }

        // Check if i,j in range 
        static bool IsSafe(int i, int j, bool[,] visitTable)
        {
            return (i >= 0 && i < M && j >= 0 && j < N && !visitTable[i, j]);
        }

        public IResults FindWords(char[,] board)
        {
            bool[,] visitTable = new bool[M, N];   // Mark all characters as not visited
            TrieNode p = root;
            String str = "";

            // Traverse through the matrix
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    // Find character of word in dictionary which is child of Trie root 
                    if (p.Child[(board[i, j]) - 'a'] != null)
                    {
                        str = str + board[i, j];
                        SearchWord(p.Child[(board[i, j]) - 'a'], board, i, j, visitTable, str);
                        str = "";
                    }
                }
            }
            return new ResultsTable();
        }

        // Main Method to run the code 
        public static void Main(String[] args)
        {
            string filePath = "Dictionary.txt";
            MyBoggleSolution.CreateSolver(filePath);
        }
    }
}