class Dogsay < Formula
  desc "Have an ASCII dog do your talking for you"
  homepage "https://github.com/biggomega/dogsay"
  url "https://benbotvinick.com/projects/dogsay/dogsay-1.0.tar.gz"
  sha256 "231348c2f4b803d79ca5df159a75b324e7c27ac005c33503e33ae38bc2e212b8"

  def install
    bin.install "bin/dogsay"
    prefix.install "dogsay.py"
    system "/bin/sh", "install.sh", "#{prefix}"
  end

  test do
    output = shell_output("#{bin}/dogsay test")
    assert_match "test", output
    assert_match "\\/", output
  end
end
