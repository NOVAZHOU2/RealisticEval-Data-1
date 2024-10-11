/**
 * Implement a dictionary tree for fast string retrieval and storage
 */
class Trie {
public:
    /**
     * Insert a word into the trie
     * @param word The word to be inserted
     */
    void insert(const std::string& word);

    /**
     * Search if a word exists in the trie
     * @param word The word to search
     * @return True if the word exists, false otherwise
     */
    bool search(const std::string& word) const;

    /**
     * Check if any word in the trie starts with the given prefix
     * @param prefix The prefix to check
     * @return True if there is at least one word starting with the prefix, false otherwise
     */
    bool startsWith(const std::string& prefix) const;

private:
    /**
     * Helper function to recursively insert a word into the trie
     * @param node The current node in the trie
     * @param word The word to be inserted
     * @param index The current index of the character being processed
     */
    void insertHelper(TrieNode* node, const std::string& word, size_t index);

    /**
     * Helper function to recursively search for a word in the trie
     * @param node The current node in the trie
     * @param word The word to search
     * @param index The current index of the character being processed
     * @return True if the word exists, false otherwise
     */
    bool searchHelper(const TrieNode* node, const std::string& word, size_t index) const;

    /**
     * Helper function to recursively check if any word starts with the given prefix
     * @param node The current node in the trie
     * @param prefix The prefix to check
     * @param index The current index of the character being processed
     * @return True if there is at least one word starting with the prefix, false otherwise
     */
    bool startsWithHelper(const TrieNode* node, const std::string& prefix, size_t index) const;

    TrieNode root; // Root of the trie
};

/**
 * Node representing a character in the trie
 */
struct TrieNode {
    std::unordered_map<char, TrieNode*> children; // Map to store child nodes
};