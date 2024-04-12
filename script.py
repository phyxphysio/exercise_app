def transform_env_to_github_actions(env_file_path, output_file_path):
    with open(env_file_path, "r") as env_file:
        lines = env_file.readlines()

    # Prepare the GitHub Actions format
    with open(output_file_path, "w") as output_file:
        for line in lines:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            # output_file.write(f"  {key}: ${{ secrets.{key} }}\n")
            output_file.write(f"  {key}: $" + "{{ " + f"secrets.{key}" + " }}\n")


# Example usage
env_file_path = ".env.prod"
output_file_path = ".github/secrets.yaml"
transform_env_to_github_actions(env_file_path, output_file_path)

print(f"GitHub Actions formatted variables have been written to {output_file_path}")
