import libtorrent as lt
import time

ses = lt.session()
params = lt.add_torrent_params()
params.save_path = '/downloads/'

link = "magnet:?xt=urn:btih:08DAA465F1212ECF47A98D21210741FEB3D09B71&dn=Companion+%282025%29+%5B1080p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fopen.tracker.cl%3A1337%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=https%3A%2F%2Fopentracker.i2p.rocks%3A443%2Fannounce"

atp = lt.parse_magnet_uri(link)
atp.save_path = params.save_path

handle = ses.add_torrent(atp)

while not handle.status().has_metadata:
    time.sleep(1)

while not handle.status().is_seeding:
    status = handle.status()
    print(f"{status.progress * 100:.2f}% done - {status.num_seeds} seeders, {status.num_peers} peers")
    time.sleep(2)

print("Download complete!")
