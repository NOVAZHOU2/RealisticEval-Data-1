class UniqueDeque {
private:
    std::deque<int> deque;
    std::unordered_set<int> set;

public:
    /**
     * Add an item to the deque if it is not already present.
     *
     * @param item The item to add.
     * @return bool True if the item was added, False if it was already present.
     */
    bool add(int item);

    /**
     * Remove an item from the deque if it exists.
     *
     * @param item The item to remove.
     * @return bool True if the item was removed, False if it was not found.
     */
    bool deleteItem(int item);

    /**
     * Check if an item is present in the deque.
     *
     * @param item The item to check.
     * @return bool True if the item is present, False otherwise.
     */
    bool contains(int item) const;

    /**
     * Get the number of elements in the deque.
     *
     * @return int The number of unique elements in the deque.
     */
    size_t size() const;

    /**
     * Create an iterator for the deque.
     *
     * @return auto An iterator over the elements in the deque.
     */
    auto begin();

    /**
     * Create an end iterator for the deque.
     *
     * @return auto An end iterator over the elements in the deque.
     */
    auto end();
};