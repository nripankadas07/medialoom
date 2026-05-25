from medialoom.core import render_html, scan


def test_media_catalog(tmp_path):
    (tmp_path / "Movie.Name.mp4").write_bytes(b"x")
    items = scan(tmp_path)
    assert items[0].kind == "video"
    assert "Movie Name" in render_html(items)
