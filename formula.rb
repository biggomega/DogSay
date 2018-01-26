class Dogsay < Formula
  desc "Have an ASCII dog do your talking for you"
  homepage "https://github.com/biggomega/dogsay"
  url "https://benbotvinick.com/projects/dogsay/dogsay-1.0.tar.gz"
  sha256 "6fe309a20bdd944f8afa10abc67a5048c8da21e764e6aa7f2bed4d8772f84965"

  def install
    bin.install("bin/dogsay")
  end

  test do
    output = shell_output("#{bin}/dogsay test")
    assert_match "test", output
    assert_match "\\/", output
  end
end
