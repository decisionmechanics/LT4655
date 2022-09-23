import cProfile
import cProfile
import pstats
from nth_prime import main as find_nth_prime

cProfile.run(f"find_nth_prime({100_000})", "stats")
profile_statistics = pstats.Stats("stats")
profile_statistics.sort_stats(pstats.SortKey.TIME).print_stats()
profile_statistics.dump_stats("stats.out")
