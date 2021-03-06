# School Report Generator

# Client Requirements

Given a commma separated string of values, return the school report in the format as shown below.

"Green: 1"
"Amber: 1"
"Red: 1"

Input example: "Green, Green, Red, Amber, Red"

> ✅ - When given a "Green" score return "Green: 1"

|  Input  |   Output   |
| :-----: | :--------: |
| "Green" | "Green: 1" |

> ✅ - When given a "Amber" score return "Amber: 1"

|  Input  |   Output   |
| :-----: | :--------: |
| "Amber" | "Amber: 1" |

> ✅ - When given a "Red" score return "Red: 1"

| Input |  Output  |
| :---: | :------: |
| "Red" | "Red: 1" |

> ✅ - When given a "Green, Green" score return "Green: 2"

|     Input      |   Output   |
| :------------: | :--------: |
| "Green, Green" | "Green: 2" |

> ✅ - When given a "Amber, Amber" score return "Amber: 2"

|     Input      |   Output   |
| :------------: | :--------: |
| "Amber, Amber" | "Amber: 2" |

> ✅ - When given a "Red, Red" score return "Red: 2"

|   Input    |  Output  |
| :--------: | :------: |
| "Red, Red" | "Red: 2" |

> ✅ - When given a "Red, Red, Green, Amber, Green" score return "Green: 2\nAmber: 1\nRed: 2"

|              Input              |            Output            |
| :-----------------------------: | :--------------------------: |
| "Red, Red, Green, Amber, Green" | "Green: 2\nAmber: 1\nRed: 2" |

**Edge Cases**

- results are always capitalized

# Technology

- Python 3.8
- Pytest 5.4
