# Data-Mining-BAUET-CSE14th-Lab

Data-Mining-BAUET-CSE14th-Lab

[Tanvir Anjom Siddique (Alvi)](https://www.linkedin.com/in/tanvir-anjom-siddique-50028a205/)

<div>
<h3>Solve Commit Error: Max Path Length Limit</h3>
Windows has a maximum path length limit (260 characters).
If your file path is extremely long due to many nested folders and a long file name, Git cannot process it.

- Enable long paths in Git:
  ```bash
      git config --system core.longpaths true
  ```
- Make sure Windows long path support is enabled:
  - Press Windows + R, type gpedit.msc (if available).
  - Navigate to:
  ```bash
      Local Computer Policy >
      Computer Configuration >
      Administrative Templates >
      System >
      Filesystem >
      Enable Win32 long paths
  ```
- Set it to Enabled and restart your computer.
- After fixing, verify by running:

  ```bash
      git add .
      git commit -m "Added files successfully"
  ```

- If Git no longer shows “filename too long”, your configuration will work.
</div>
