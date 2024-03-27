## 1 A+B问题I

```cpp
#include<iostream>
using namespace std;
int main() {
    int a, b;
    while(cin >> a >> b) {
        int result = a + b;
        cout << result << endl;
    }
    return 0;
}
```

## 2. A+B问题II

```cpp
#include<iostream>
using namespace std;
int main() {
    int N, a, b;
    while(cin >> N) {
        while(N--) {
            cin >> a >> b;
            cout << a+b << endl;
        }
    }
    return 0;
}
```

## 3 A+B问题III
```cpp
#include<iostream>
using namespace std;
int main() {
    int a, b;
    while(cin >> a >> b){
        if(!a && !b) break;
        cout << a+b << endl;
    }
    return 0;
}
```

## 4 A+B问题IV

```cpp
#include<iostream>
using namespace std;
int main() {
    int n, a;
    while(cin >> n) {
        if(n == 0) break;
        int sum = 0;
        while(n--) {
            cin >> a;
            sum += a;
        }
        cout << sum << endl;
    }
}
```

## 5 A+B问题V

```cpp
#include<iostream>
using namespace std;
int main() {
    int a, b;
    while(cin >> a >>b){
        cout << a+b << endl << endl;
    }
    return 0;
}
```

## 6 A+B问题VI

```ad-note
本题是前面五道题的综合考察，`问题一`考察如何获取输入编写输出，`问题二`考察如何获取指定数目的有限输入 和 处理连续不断地测试用例输入，`问题三`考察如何获取给定结尾条件的输入，`问题四`综合考察指定数目有限输入 和 处理连续不断地测试用例输入 以及 给定结尾条件输入，`问题五`考察如何输入空行，`问题六`综合考察以上所有。
```

```cpp
#include<iostream>
using namespace std;
int main() {
    int n, m, a;
    while(cin >> n){
        while(n--){
            cin >> m;
            int sum = 0;
            while(m--){
                cin >> a;
                sum += a;
            }
            cout << sum << endl;
            if(n > 0) cout << endl;
        }
    }
}
```

## 7 平均绩点

```ad-note
本题考查点有很多，包括 `标准库容器头文件的引用`，`字符串的按行读取(不包含换行符)`，`使用C中printf函数对浮点数精度做限制`, `使用iomanip格式化输入输出cin和cout`
```

```cpp
#include<iostream>
// #include<iomanip>
#include<unordered_map>
#include<string>
using namespace std;
int main (){
    unordered_map<char, int> map = {
        {'A', 4},
        {'B', 3},
        {'C', 2},
        {'D', 1},
        {'F', 0},
    };
    string str;
    while(getline(cin, str)) {
        float sum = 0;
        int count = 0;
        bool flag = true;
        for(int i = 0; i < str.size(); i++){
            if(str[i] == ' ') continue;
            if(map.find(str[i]) != map.end()) {
                sum += map[str[i]];
                count++;
            }else{
                flag = false;
                break;
            }
        }
        if(flag) 
	        printf("%.2f\n", sum / count);
	        // cout << fixed << setprecision(2) << sum/count << endl;
        else 
	        cout << "Unknown" << endl;      
    }
    return 0;
}
```

## 8 摆平积木

```cpp
#include<iostream>
#include<vector>
using namespace std;
int main() {
    int n;
    while(cin >> n){
        if(n == 0)break;
        vector<int> nums;
        int count = 0;
        int sum = 0;
        int a;
        while(n--) {
            cin >> a;
            nums.push_back(a);
            sum += a;
            count++;
        }
        int result = 0;
        int avg = sum/count;
        for(int& num:nums) {
            if(num < avg) result += (avg - num);
        }
        cout << result << endl;
        cout << endl;
    }
    return 0;
}
```

## 9 奇怪的信

```cpp
#include<iostream>
#include<string>
using namespace std;
int main() {
    string str;
    while(getline(cin, str)) {
        int sum = 0;
        for(int i = 0; i < str.size(); i++) {
            if((str[i] - '0') % 2 == 0) {
                sum += (str[i] - '0');
            }
        }
        cout << sum << endl;
        cout << endl;
    }
}
```

## 10 运营商活动

```cpp
// 求解
#include<iostream>
using namespace std;
int main () {
    int k, m;
    while(cin >> k >> m) {
        if(!k && !m) break;
        int money = k; // 未兑换话费
        int plus = money / m; // 赠送话费
        while(plus != 0) {
            k += plus; // 更新总话费
            money = money % m + plus;
            plus = money / m;
        }
        cout << k << endl;
    }
    return 0;
}
```

## 11 共同祖先

```cpp
#include<iostream>
#include<vector>
using namespace std;
int main () {
    int n; // 行数
    vector<int> nums(21, 0);
    int a, b;
    while(cin >> n) {
        while(n--) {
            cin >> a >> b;
            nums[a] = b;
        }
        int ming = nums[1];
        int yu = nums[2];
        int len_ming = 0;
        int len_yu = 0;
        while(ming != 0) {
            ming = nums[ming];
            len_ming++;
        }
        while(yu != 0) {
            yu = nums[yu];
            len_yu++;
        }
        if(len_ming > len_yu) {
            cout << "You are my elder" << endl;
        }else if(len_ming < len_yu) {
            cout << "You are my younger" << endl;
        }else {
            cout << "You are my brother" << endl;
        }
    }
    return 0;
}
```

## 12 打印数字图形

```cpp
#include<iostream>
using namespace std;
int main () {
    int n;
    while(cin >> n) {
        int space = n-1; // 可打印空格数
        int num = 1; // 可打印最大数字
        for(int i = 0; i < n; i++) { // 行数
            for(int i = 0; i < space; i++) { // 空格数
                printf(" ");
            }
            for(int i = 1; i <= num; i++) { // 前数字
                printf("%d", i);
            }
            for(int i = num-1; i > 0; i--) { // 后数字
                printf("%d", i);
            }
            cout << endl;
            space--;
            num++;
        }
        space = 1;
        num -= 2;
        for(int i = n-1; i > 0; i--) { // 行数
            for(int i = 0; i < space; i++) { // 空格数
                printf(" ");
            }
            for(int i = 1; i <= num; i++) { // 前数字
                printf("%d", i);
            }
            for(int i = num-1; i > 0; i--) { // 后数字
                printf("%d", i);
            }
            cout << endl;
            space++;
            num--;
        }
    }
    return 0;
}
```

## 13 镂空三角形

```cpp
#include<iostream>
using namespace std;
int main () {
    char ch;
    int n;
    while(cin >> ch) {
        if(ch == '@') break;
        cin >> n;     
        if(n > 1) {
            for(int j = 0; j < n-1; j++) { // 打印第一行
                cout << " ";
            } 
            cout << ch << endl;
        }
        for(int i = 2; i <= n-1; i++) { // 打印中间
            for(int j = 0; j < n-i; j++) {
                cout << " ";
            }
            cout << ch;
            for(int j = 0; j < (2*i-3); j++) {
                cout << " ";
            }
            cout << ch;
            cout << endl;
        }
        for(int i = 0; i < (2*n-1); i++) { // 空格
            cout << ch;
        }
        cout << endl;
        cout << endl;
    }
    return 0;
}
```

## 14 句子缩写

```ad-note
本题考察点有 `字符库cctype的使用`, `忽略读取到换行符前字符cin.ignore()的使用`
```

```cpp
#include<iostream>
#include<cctype>
#include<string>
using namespace std;
int main () {
    int n;
    cin >> n;
    cin.ignore();
    while(n--) {
        string str;
        string res;
        getline(cin, str);
        for(int i = 0; i < str.size(); i++) {
            if(!i && isalpha(str[i])) res += toupper(str[i]);
            if(i > 0 && isalpha(str[i]) && str[i-1] == ' ') 
                res += toupper(str[i]);
        }
        cout << res << endl;
    }
    return 0;
}
```

# 15 神秘字符

```cpp
#include<iostream>
#include<string>
using namespace std;
int main () {
    int n;
    cin >> n;
    cin.ignore();
    while(n--) {
        string str1, str2;
        string res;
        getline(cin, str1);
        getline(cin, str2);
        res += str1.substr(0, str1.size()/2);
        res += str2;
        res += str1.substr(str1.size()/2, str1.size()/2);
        cout << res << endl;
    }
    return 0;
}
```

# 16 位置互换
```cpp
#include<iostream>
#include<string>
using namespace std;
int main () {
    int n;
    cin >> n;
    cin.ignore();
    while(n--) {
        string str;
        getline(cin, str);
        for(int i = 1; i < str.size(); i+=2) {
            swap(str[i], str[i-1]);
        }
        cout << str << endl;
    }
    return 0;
}
```

# 17 出栈合法性
```cpp
#include<iostream>
#include<stack>
using namespace std;
int main () {
    int n;
    int nums[100];
    while(cin>>n, n) {
        for(int i = 0; i < n; i++) {
            cin >> nums[i];
        }
        stack<int> stk;
        for (int i = 1, j = 0; i <= n; i++) {
            stk.push(i);
            while (!stk.empty() && stk.top() == nums[j]) {
                stk.pop();
                j++;
            }
        }
        if(stk.empty()) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
    return 0;
}
```

# 18 链表的基本操作

```cpp
#include<iostream>
#include<string>
using namespace std;
class LinkedList {
public:
	struct ListNode {
		int val;
		ListNode* next;
		ListNode(int x): val(x), next(NULL) {};
	};
	
	LinkedList() {
		size = 0;
		dummyNode = new ListNode(0);
	}
	
	int get(int x) {
		ListNode* cur = dummyNode;
		if(x > size || x <= 0) {
			cout << "get fail" << endl;
			return 0;
		}
		for(int i = 0; i < x; i++) {
			cur = cur->next;
		}
		return cur->val;
	}

	void deleteNode(int x) {
		ListNode* cur = dummyNode;
		if(x > size || x <= 0) {
			cout << "delete fail" << endl;
			return;
		}
		for(int i = 0; i < x-1; i++) {
			cur = cur->next;
		}
		ListNode* tmp = cur->next;
		cur->next = tmp->next;
		delete tmp;
		tmp = NULL;
		size--;
		cout << "delete OK" << endl;
	}
	void insert(int a, int e, bool flag = true) {
		ListNode* cur = dummyNode;
		if(a > size+1 || a <= 0) {
			cout << "insert fail" << endl;
			return;
		}
		for(int i = 0; i < a-1; i++) {
			cur = cur->next;
		}
		ListNode* tmp = cur->next;
		ListNode* node = new ListNode(e);
		cur->next = node;
		node->next = tmp;
		size++;
		if(flag) cout << "insert OK" << endl;
	}
	void show() {
		ListNode* cur = dummyNode->next;
		if(cur == NULL) {
			cout << "Link list is empty" << endl;
			return;
		}
		while(cur != NULL) {
			cout << cur->val << " ";
			cur = cur->next;
		}
		cout << endl;
	}
private:
    ListNode* dummyNode;
    int size;
};

int main () {
    int n, m;
    int num;

    LinkedList ls;
    // 初始化
    cin >> n;
    while(n--) {
        cin >> num;
        ls.insert(1, num, false);
    }
    // 操作
    string op;
    int a, e, x;
    cin >> m;
    while(m--) {
        cin >> op;
        if(op == "show") {
            ls.show();
        }
        if(op == "delete") {
            cin >> x;
            ls.deleteNode(x);
        }
        if(op == "insert") {
            cin >> a >> e;
            ls.insert(a, e);
        }
        if(op == "get") {
            cin >> x;
            cout << ls.get(x) << endl;
        }
    }
    return 0;
}
```


# 19 链表反转

```cpp
#include<iostream>
#include<string>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL){}
};

int main() {
    string str;
    int n;
    while(cin >> n) {
        if(n == 0) {
            cout << "list is empty" << endl;
            continue;   
        }
        // 创建链表
        int num;
        ListNode* dummyNode = new ListNode(0);
        ListNode* cur = dummyNode;
        while(n--) {
            cin >> num;
            ListNode* node = new ListNode(num);
            cur->next = node;
            cur = cur->next;
        }
        // 打印链表
        cur = dummyNode->next;
        while(cur!=NULL) {
            cout << cur->val << " ";
            cur = cur->next;
        }
        cout << endl;
        // 反转链表
        ListNode* pre = nullptr;
        cur = dummyNode->next;
        ListNode* tmp;
        while(cur != NULL) {
            tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        
        // 打印链表
        while(pre!=NULL) {
            cout << pre->val << " ";
            pre = pre->next;
        }
        cout << endl;
        
        
    }
}
```

# 20 删除重复元素
```cpp
#include<iostream>
using namespace std;
struct Node {
    int val;
    Node* next;
    Node(int _val = 0) {
        val = _val;
        next = nullptr;
    }
};
int main(){
    int n, x;
    while (cin >> n) {
        if (n == 0) {
            cout << "list is empty" << endl;
            continue;
        }     
        //构建链表
        Node* dummy = new Node(-1), *curr = dummy, *prev = nullptr;
        while (n--) {
            cin >> x;
            
            cout << x << " ";   //  输出删除前的链表元素
            
            //跳过重复元素
            //保持链表的递增性
            if (curr->val < x) {
                curr->next = new Node(x);
                prev = curr;
                curr = curr->next;
            }
        }
        cout << endl;
        //输出删除后的链表元素
        curr = dummy->next;
        while (curr) {
            cout << curr->val << " ";
            curr = curr->next;
        }
        cout << endl;
    }  
    return 0;
}
```
