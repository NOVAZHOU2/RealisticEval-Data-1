public class UniqueDeque<T> {

    private Deque<T> deque = new LinkedList<>();

    /**
     * Add an item to the deque if it is not already present.
     *
     * @param item The item to add.
     * @return boolean True if the item was added, False if it was already present.
     */
    public boolean add(T item) {
        if (!deque.contains(item)) {
            deque.addLast(item);
            return true;
        }
        return false;
    }

    /**
     * Remove an item from the deque if it exists.
     *
     * @param item The item to remove.
     * @return boolean True if the item was removed, False if it was not found.
     */
    public boolean delete(T item) {
        return deque.remove(item);
    }

    /**
     * Check if an item is present in the deque.
     *
     * @param item The item to check.
     * @return boolean True if the item is present, False otherwise.
     */
    public boolean contains(T item) {
        return deque.contains(item);
    }

    /**
     * Get the number of elements in the deque.
     *
     * @return int The number of unique elements in the deque.
     */
    @Override
    public int size() {
        return deque.size();
    }

    /**
     * Create an iterator for the deque.
     *
     * @return Iterator<T> An iterator over the elements in the deque.
     */
    @Override
    public java.util.Iterator<T> iterator() {
        return deque.iterator();
    }
}