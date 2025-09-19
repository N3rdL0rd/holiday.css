import os
import glob

MODERN_NORMALIZE_PATH = 'node_modules/modern-normalize/modern-normalize.css'
SRC_CSS_PATH = 'src/css/*.css'
THEMES_PATH = 'src/css/themes/'
DIST_PATH = 'dist/'

def build_css():
    """
    Concatenates CSS files to generate a default and themed builds.
    """
    if not os.path.exists(DIST_PATH):
        os.makedirs(DIST_PATH)

    base_css_files = sorted(glob.glob(SRC_CSS_PATH))

    print("Building dist/holiday.css...")
    with open(os.path.join(DIST_PATH, 'holiday.css'), 'w') as outfile:
        with open(MODERN_NORMALIZE_PATH, 'r') as infile:
            outfile.write(infile.read())
            outfile.write('\n')

        for css_file in base_css_files:
            with open(css_file, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')

        with open(os.path.join(THEMES_PATH, 'bulma.css'), 'r') as infile:
            outfile.write(infile.read())
            outfile.write('\n')
    print("Successfully created dist/holiday.css")

    theme_files = sorted(glob.glob(os.path.join(THEMES_PATH, '*.css')))

    for theme_file in theme_files:
        theme_name = os.path.basename(theme_file).replace('.css', '')

        if theme_name == 'bulma':
            continue

        output_filename = f'holiday_{theme_name}.css'
        print(f"Building {os.path.join(DIST_PATH, output_filename)}...")

        with open(os.path.join(DIST_PATH, output_filename), 'w') as outfile:
            with open(MODERN_NORMALIZE_PATH, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')

            for css_file in base_css_files:
                with open(css_file, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')

            with open(theme_file, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')
        print(f"Successfully created {os.path.join(DIST_PATH, output_filename)}")


if __name__ == "__main__":
    build_css()