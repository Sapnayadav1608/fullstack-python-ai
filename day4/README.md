# ⏱️ Day 04: Time & Space Complexity — Big O Fundamentals

30-Day Full Stack + AI Engineering Challenge | **Day 4: Algorithm Analysis & Optimization**

---

## 📚 Topics & Modules Covered Today

| # | File Name | Key Concepts |
| :-: | :--- | :--- |
| **01** | [`01_big_o_fundamentals.py`](./01_big_o_fundamentals.py) | Why seconds/stopwatch measurement is flawed, operations count as function of $N$, Big O, Big $\Omega$, Big $\Theta$ |
| **02** | [`02_common_time_complexities.py`](./02_common_time_complexities.py) | Order of Growth: $O(1)$ constant, $O(\log n)$ binary search, $O(n)$ linear, $O(n \log n)$ sorting, $O(n^2)$ quadratic, $O(2^n)$ exponential |
| **03** | [`03_rules_for_calculating_big_o.py`](./03_rules_for_calculating_big_o.py) | The 4 Golden Rules: Drop constants ($O(2N) \rightarrow O(N)$), drop non-dominant terms, Add ($O(A+B)$) vs Multiply ($O(A \times B)$) |
| **04** | [`04_space_complexity_and_call_stack.py`](./04_space_complexity_and_call_stack.py) | Auxiliary Space vs Input Space, recursion call stack memory $O(N)$ vs iteration $O(1)$, string memory traps |
| **05** | [`05_code_analysis_case_studies.py`](./05_code_analysis_case_studies.py) | **Case Study:** Two Sum Problem ($O(N^2)$ brute-force vs $O(N)$ Hash Map optimization with live speed comparison) |
| **06** | [`06_live_benchmarking_tool.py`](./06_live_benchmarking_tool.py) | Visual ASCII performance table comparing $O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$ on live inputs |
| **07** | [`07_interview_big_o_questions.py`](./07_interview_big_o_questions.py) | Top tricky interview questions: $i *= 2$ loops, triangle loops, string concatenation $+=$ trap, `in list` vs `in set` |
| **WORKBOOK** | [`my_practice.py`](./my_practice.py) | **Self-Practice Workbook:** 5 Hands-on analysis and optimization tasks with TODO sections |

---

## 🏃 How to Run Any File

Terminal mein run karein:

```powershell
python day4\01_big_o_fundamentals.py
python day4\06_live_benchmarking_tool.py
python day4\my_practice.py
```
