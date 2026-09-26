# Project Diagrams

## Main Flow
```text
START
 |
 +--> Register --> Save User
 |
 +--> Login --> Check User --> Expense Menu
 |                              +--> Add
 |                              +--> View
 |                              +--> Search
 |                              +--> Update
 |                              +--> Delete
 |                              +--> Summary
 |                              +--> Monthly Summary
 |                              +--> Save
 |                              +--> Logout
 |
 +--> Exit --> END
```

## Data Flow
```text
Input -> Validation -> Lists/Dictionaries -> Functions -> Text Files -> Output
```
