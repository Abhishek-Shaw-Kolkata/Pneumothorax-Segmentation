# Pneumothorax-Segmentation
### Identify Pneumothorax disease in chest x-rays
## Business/Real-world Problem
Imagine suddenly gasping for air, helplessly breathless for no apparent reason. Could it be a collapsed lung?
Pneumothorax can be caused by a blunt chest injury, damage from underlying lung disease, or most horrifying - it may occur for no obvious reason at all. On some occasions, a collapsed lung can be a life-threatening event.
Pneumothorax is usually diagnosed by a radiologist on a chest x-ray, and can sometimes be very difficult to confirm. An accurate AI algorithm to detect Pneumothorax would be useful in a lot of clinical scenarios. AI could be used to triage chest radio graphs for priority interpretation, or to provide a more confident diagnosis for non-radiologists.

The Society for Imaging Informatics in Medicine (SIIM) is the leading healthcare organization for those interested in the current and future use of informatics in medical imaging. Their mission is to advance medical imaging informatics across the enterprise through education, research, and innovation in a multi-disciplinary community.
In this competition, we'll develop a model to classify (and if present, segment) Pneumothorax from a set of chest radio graphic images. If successful, we could aid in the early recognition of Pneumothoraces and save lives.
It requires a lot of effort to determine certain cases of Pneumothorax where the affected area is minimal and it also requires good domain experts. So having an AI enabled system will help radiologists by reducing the time required to run diagnostic tests and also reduce the chances of errors. The algorithm had to be extremely accurate because lives of people is at stake.
## Business objectives and constraints
__Objectives:__
We need to predict Pneumothorax from a set of chest radio graphic images and if it is present we need to segment that also
Minimize Dice coefficient.

Constraints:
1. Since it's a medical domain problem so predicting False Negatives  is a big issue.
2. No strict latency constraints.

## For more detailed explanation you can visit to my medium blog at
