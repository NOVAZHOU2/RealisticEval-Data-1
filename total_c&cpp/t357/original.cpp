// Built upon code generated by ChatGPT
template <typename T>
Sort_stats shell_sort(vector<T> &v)
{
    ulong num_comps = 0;
    clock_t start = clock();

    int n = v.size();

    for (int gap = n / 2; gap > 0; gap /= 2)
    {
        for (int i = gap; i < n; i++)
        {
            T temp = v[i];
            int j = i;

            num_comps++;
            while (j >= gap && v[j - gap] > temp)
            {
                v[j] = v[j - gap];
                j -= gap;
            }

            v[j] = temp;
        }
    }

    clock_t end = clock();
    double elapsed_cpu_time_sec = double(end - start) / CLOCKS_PER_SEC;

    return Sort_stats{"Shell sort", v.size(), num_comps, elapsed_cpu_time_sec};
}
