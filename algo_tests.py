import unittest
import time
from p2_with_invariant import knuth_p1, knuth_p2

class TestKnuthAlgorithms(unittest.TestCase):
    def test_single_value(self):
        """Test a single value to demonstrate the algorithm"""
        n = 8132
        decimal, digits, k = knuth_p2(n)
        n_back = knuth_p1(decimal)
        self.assertEqual(n, n_back, f"Failed for {n}, got {n_back} back")
        print(f"n={n} converts to {decimal} with {k} digits and converts back to {n_back}")
    
    def test_range(self):
        """Test a range of values to verify round-trip conversions"""
        # Testing a smaller range by default to keep execution time reasonable
        # Change this to test more values
        start = 1
        end = 1000  # Adjust this value to test more numbers (up to 65535)
        
        start_time = time.time()
        total = end - start + 1
        tested = 0
        mismatches = []
        
        for n in range(start, end + 1):
            decimal, _, _ = knuth_p2(n)
            n_back = knuth_p1(decimal)
            
            if n != n_back:
                mismatches.append((n, n_back))
            
            tested += 1
            
            # Print progress for longer tests
            if tested % 1000 == 0 and end > 1000:
                elapsed = time.time() - start_time
                print(f"Tested {tested}/{total} values ({tested/total:.1%}) - {elapsed:.2f} seconds elapsed")
        
        elapsed = time.time() - start_time
        print(f"\nTesting complete: {tested} values tested in {elapsed:.2f} seconds")
        
        # Report any mismatches
        if mismatches:
            mismatch_str = "\n".join([f"n={n}, got {n_back}" for n, n_back in mismatches])
            self.fail(f"Found {len(mismatches)} mismatches:\n{mismatch_str}")
    
    def test_full_range(self):
        """Test the full range from 1 to 65535 (disabled by default)"""
        # Skip this test by default as it takes a long time
        # Remove this line to run the full test
        self.skipTest("Skipping full range test (1-65535) to save time")
        
        start_time = time.time()
        total = 65535
        tested = 0
        mismatches = []
        
        for n in range(1, 65536):
            decimal, _, _ = knuth_p2(n)
            n_back = knuth_p1(decimal)
            
            if n != n_back:
                mismatches.append((n, n_back))
            
            tested += 1
            
            # Print progress every 10,000 values
            if tested % 10000 == 0:
                elapsed = time.time() - start_time
                print(f"Tested {tested}/{total} values ({tested/total:.1%}) - {elapsed:.2f} seconds elapsed")
        
        elapsed = time.time() - start_time
        print(f"\nTesting complete: {tested} values tested in {elapsed:.2f} seconds")
        
        # Assert that there are no mismatches
        if mismatches:
            mismatch_str = "\n".join([f"n={n}, got {n_back}" for n, n_back in mismatches[:10]])
            if len(mismatches) > 10:
                mismatch_str += f"\n... and {len(mismatches) - 10} more"
            self.fail(f"Found {len(mismatches)} mismatches:\n{mismatch_str}")

if __name__ == "__main__":
    unittest.main(verbosity=2)