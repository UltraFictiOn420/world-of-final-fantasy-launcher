"""Build a deterministic source-only release archive; never runs the game."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"
FILES = (
    "Launch-WoFF.bat", "steam_appid.txt", "README.md", "LICENSE",
    "SECURITY.md", "CHANGELOG.md", "docs/TESTING.md", "docs/PROJECT_MAP.md",
)


def release_bytes(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    if path.endswith(".bat"):
        return text.replace("\r\n", "\n").replace("\n", "\r\n").encode("ascii")
    return text.replace("\r\n", "\n").encode("utf-8")


def build():
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    archive = dist / f"WoFF-Standard-User-Launcher-v{VERSION}.zip"
    contents = {path: release_bytes(path) for path in FILES}
    manifest = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {path}\n"
        for path, data in contents.items()
    )
    contents["CHECKSUMS.sha256"] = manifest.encode("ascii")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path, data in contents.items():
            info = zipfile.ZipInfo(path, date_time=(2026, 10, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, data)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (dist / f"{archive.name}.sha256").write_text(
        f"{digest}  {archive.name}\n", encoding="ascii"
    )
    print(f"{archive.name}: {digest}")
    return archive


if __name__ == "__main__":
    build()
