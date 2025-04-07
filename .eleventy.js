module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.addPassthroughCopy("favicon.ico");
  eleventyConfig.addPassthroughCopy("favicon-16x16.png");
  eleventyConfig.addPassthroughCopy("favicon-32x32.png");
  eleventyConfig.addPassthroughCopy("nyan-cat.mp4");
  eleventyConfig.addPassthroughCopy("sample.pdf");
  eleventyConfig.addPassthroughCopy("t-rex-roar.mp3");
  eleventyConfig.addPassthroughCopy("dist/holiday.css");

  return {
    dir: {
      input: "site",
    },
  };
};
