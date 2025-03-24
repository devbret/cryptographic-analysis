import string
import collections
import logging

def frequency_analysis(text):
    filtered_text = ''.join([c for c in text.upper() if c in string.ascii_uppercase])
    frequencies = collections.Counter(filtered_text)
    total = sum(frequencies.values())
    frequency_table = {char: freq / total for char, freq in frequencies.items()} if total > 0 else {}
    return frequency_table

def index_of_coincidence(text):
    filtered_text = ''.join([c for c in text.upper() if c in string.ascii_uppercase])
    N = len(filtered_text)
    if N <= 1:
        return 0
    frequencies = collections.Counter(filtered_text)
    ic = sum([freq * (freq - 1) for freq in frequencies.values()]) / (N * (N - 1))
    return ic

def caesar_brute_force(text):
    text = text.upper()
    results = {}
    for shift in range(26):
        decrypted = ''
        for char in text:
            if char in string.ascii_uppercase:
                decrypted += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted += char
        results[shift] = decrypted
    return results

def bigram_analysis(text):
    filtered_text = ''.join([c for c in text.upper() if c in string.ascii_uppercase])
    bigrams = [filtered_text[i:i+2] for i in range(len(filtered_text) - 1)]
    bigram_counts = collections.Counter(bigrams)
    total = sum(bigram_counts.values())
    bigram_table = {bigram: count / total for bigram, count in bigram_counts.items()} if total > 0 else {}
    return bigram_table

def chi_squared_caesar(text):
    english_freq = {
        'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
        'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
        'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
        'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
        'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974,
        'Z': 0.00074
    }
    
    results = {}
    text = text.upper()
    for shift in range(26):
        decrypted = ''
        for char in text:
            if char in string.ascii_uppercase:
                decrypted += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted += char
        
        # Count frequencies in the decrypted text
        filtered = [c for c in decrypted if c in string.ascii_uppercase]
        total = len(filtered)
        if total == 0:
            chi_squared = float('inf')
        else:
            observed = collections.Counter(filtered)
            chi_squared = 0
            for letter in string.ascii_uppercase:
                O = observed.get(letter, 0)
                E = total * english_freq[letter]
                if E > 0:
                    chi_squared += ((O - E) ** 2) / E
        results[shift] = (decrypted, chi_squared)
    return results

def main():
    logging.basicConfig(filename='crypto_analysis.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting Cryptographic Analysis Tool")
    
    # Hard-coded file paths
    file_path = "/file/path/to/encrypted-text.txt"
    output_file = "crypto_results.txt"
    
    try:
        with open(file_path, 'r') as file:
            ciphertext = file.read()
        logging.info(f"Read ciphertext from {file_path}")
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        print(f"Error reading file: {e}")
        return

    result_lines = []
    result_lines.append("Cryptographic Analysis Tool")
    result_lines.append("=============================")
    result_lines.append("Ciphertext:")
    result_lines.append(ciphertext)
    result_lines.append("")

    # Frequency Analysis
    logging.info("Performing frequency analysis")
    freq = frequency_analysis(ciphertext)
    result_lines.append("Frequency Analysis:")
    for char in sorted(freq.keys()):
        result_lines.append(f"{char}: {freq[char]:.2%}")
    result_lines.append("")

    # Index of Coincidence
    logging.info("Calculating Index of Coincidence")
    ic = index_of_coincidence(ciphertext)
    result_lines.append("Index of Coincidence: {:.4f}".format(ic))
    result_lines.append("")

    # Caesar Cipher Brute Force
    logging.info("Performing Caesar cipher brute force")
    result_lines.append("Caesar Cipher Brute Force:")
    caesar_results = caesar_brute_force(ciphertext)
    for shift, decrypted_text in caesar_results.items():
        result_lines.append(f"Shift {shift:2}: {decrypted_text}")
    result_lines.append("")

    # Bigram Analysis
    logging.info("Performing bigram analysis")
    bigram_freq = bigram_analysis(ciphertext)
    result_lines.append("Bigram Frequency Analysis:")
    for bigram, freq_val in sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True):
        result_lines.append(f"{bigram}: {freq_val:.2%}")
    result_lines.append("")

    # Chi-Squared Analysis for Caesar Cipher
    logging.info("Performing chi-squared analysis for Caesar cipher")
    chi_results = chi_squared_caesar(ciphertext)
    result_lines.append("Caesar Cipher Chi-Squared Analysis:")
    best_shift = None
    best_chi = float('inf')
    for shift, (decrypted_text, chi_value) in chi_results.items():
        result_lines.append(f"Shift {shift:2}: Chi-Squared = {chi_value:.2f}")
        if chi_value < best_chi:
            best_chi = chi_value
            best_shift = shift
    if best_shift is not None:
        result_lines.append("")
        result_lines.append(f"Best shift according to chi-squared: Shift {best_shift} with Chi-Squared = {best_chi:.2f}")
        result_lines.append("Decrypted Text:")
        result_lines.append(chi_results[best_shift][0])
    result_lines.append("")

    # Write results to output file
    try:
        with open(output_file, 'w') as out_file:
            out_file.write("\n".join(result_lines))
        logging.info(f"Results written to {output_file}")
    except Exception as e:
        logging.error(f"Error writing output file: {e}")
        print(f"Error writing output file: {e}")
    
    # Print results to the console
    print("\n".join(result_lines))

if __name__ == '__main__':
    main()
