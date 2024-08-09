#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,j;
    ifstream fin("input.txt");
    string num;
    cout<<"Input: "<<'\n';
    int count = 1;
    vector<string> a;
    while(getline(fin,num))
    {
        cout<<count<<")\t"<<num<<'\n';
        a.push_back(num);
        count++;
    }
    map<int,int> mp;
    mp[0] = 0;
    int curr = 0;
    for(auto q : a)
    {
        for(i=0; i<q.size()-3; i++)
        {
            if((q[i] == 'g'&&q[i+1] == 'o'&&q[i+2] == 't'&&q[i+3] == 'o')||(q[i] == 'G'&&q[i+1] == 'O'&&q[i+2] == 'T'&&q[i+3] == 'O'))
            {
                string num = "";
                int j = i+6;
                while(q[j]>='0'&&q[j]<='9'&&j<q.size()) num+=q[j],j++;
                int temp = stoi(num);
                mp[temp-1] = 1;
            }
        }
        curr++;
    }
    vector<pair<int,string>> leaders;
    vector<vector<pair<int,string>>> blocks;
    for(auto q : mp)
    {
        leaders.push_back({q.first+1,a[q.first]});
    }
    vector<pair<int,string>> temp;
    for(i=0; i<a.size(); i++)
    {
        if(mp.count(i))
        {
            blocks.push_back(temp);
            temp.clear();
        }
        temp.push_back({i+1,a[i]});
    }
    blocks.push_back(temp);
    cout<<"\n\nLeaders:"<<'\n';
    for(auto q : leaders) cout<<q.first<<")\t"<<q.second<<'\n';
    cout<<"\nBlocks:\n"<<'\n';
    for(i=1; i<blocks.size(); i++)
    {
        cout<<"Block "<<i<<": "<<'\n';
        for(auto q : blocks[i]) cout<<q.first<<")\t"<<q.second<<'\n';
        cout<<'\n';
    }
    return 0;
}
