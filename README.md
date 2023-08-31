# posikarto
Sure, here's the provided text converted to LaTeX format:

```latex
\section{Project Summary: Road Sign Detection and Localization from Point Clouds}

\begin{lstlisting}[language=Python]
# Calculate Jakteristic features
# Add your code snippet here
\end{lstlisting}

\subsection{Overview}

This project focuses on detecting and localizing road signs within point clouds classified using the Semantikarto point cloud semantic segmentation model. The process involves extracting road sign point clouds, calculating geometric features, clustering, and finally estimating the positions of the detected road signs.

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{https://prod-files-secure.s3.us-west-2.amazonaws.com/3e97aac5-d6d1-4a51-a25f-5023ed62eb24/dbc68ffc-9e7f-4a60-895f-beb8ee3100a1/Untitled.png}
    \caption{Project Overview}
\end{figure}

\subsection{Steps}

\subsubsection{Loading and Filtering Point Cloud Data}

\begin{itemize}
    \item The project begins by loading point cloud data from specified files in a given input folder.
    \item The Semantikarto model has previously classified road signs in the point clouds using the RandLA-Net architecture.
    \item Filtering is performed to extract road sign points by retaining points labeled as road signs and removing all other classes.
\end{itemize}

% Include images here

\subsubsection{Calculating Geometric Features with Jakteristics}

\begin{itemize}
    \item Geometric features are calculated on the extracted road sign point clouds using the Jakteristics library.
    \item Features like planarity, omnivariance, and others are computed to describe the geometric characteristics of the points.
    \item A planarity threshold is set, and points below this threshold are removed to ensure high planarity.
\end{itemize}

% Include images here

\subsubsection{DBSCAN Clustering}

\begin{itemize}
    \item DBSCAN (Density-Based Spatial Clustering of Applications with Noise) clustering algorithm is applied to the filtered point clouds.
    \item The feature columns are standardized, and DBSCAN clusters the points into groups based on their spatial density.
    \item The cluster with the highest average planarity value is selected as it is likely to correspond to a road sign.
\end{itemize}

% Include images here

\subsubsection{Estimating Road Sign Positions}

\begin{itemize}
    \item For each cluster, the center point is computed by averaging the X, Y, and Z coordinates of the points.
    \item The estimated center points represent the positions of the detected road signs.
    \item These center points are collected and saved in a CSV file for further analysis.
\end{itemize}

% Include images here

\subsection{Workflow}

\begin{enumerate}
    \item \textbf{Loading and Filtering}: Load point cloud data and extract road sign points based on classification results.
    \item \textbf{Geometric Feature Calculation}: Compute geometric features on the road sign points using Jakteristics.
    \item \textbf{DBSCAN Clustering}: Apply DBSCAN clustering to identify clusters with high planarity.
    \item \textbf{Estimating Positions}: Calculate center points of clusters as the estimated road sign positions.
\end{enumerate}

\subsection{Libraries Used}

\begin{itemize}
    \item Semantikarto: Point cloud semantic segmentation model using RandLA-Net.
    \item Jakteristics: Library for calculating geometric features on point clouds.
    \item Jaklas: Library for reading, processing, and writing point cloud files.
    \item pandas: Library for data manipulation and analysis.
    \item scikit-learn: Library for machine learning algorithms, including DBSCAN.
\end{itemize}

\subsection{Output}

The output of the project is a collection of estimated road sign positions in the form of center points. These positions are saved in CSV files, providing valuable information for road sign localization in the given point clouds.

This project integrates machine learning techniques for classification and clustering with geometric analysis to enable accurate road sign detection and precise localization within point clouds.

\subsection{Evaluation Function}

\subsubsection{Using csv\_evaluation.py}

This evaluation function requires users to select a ground truth and enter its coordinates in a CSV file. Common practice is to use CloudCompare for obtaining a ground truth point. The function then takes the distance between the ground truth and estimated position to evaluate the accuracy of the prediction produced by Posikarto.

\begin{lstlisting}[language=Python]
python csv_evaluation.py roadsign_1_groundtruth_center_points.csv roadsign_1_estimated_center_points.csv
\end{lstlisting}

% Include images here

\subsubsection{Using evaluation\_function.py}

This evaluation function allows users to enter a .laz file (ground truth) and the .csv of the predicted position. The function aims to determine a ground truth by normalizing the point cloud and computing the coordinate averages. The function then takes the distance between the ground truth and estimated position to evaluate the accuracy of the prediction produced by Posikarto.

\begin{lstlisting}[language=Python]
python evaluation_function.py roadsigns_data_1.laz center_points.csv
\end{lstlisting}

\begin{lstlisting}[language=Python]
[0    0.047326 dtype: float64, 
 0   -0.075733 dtype: float64, 
 0   -0.708584 dtype: float64]
\end{lstlisting}

\subsection{Installation}

\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}[language=bash]
    git clone <https://github.com/yourusername/road-sign-detection.git>
    cd road-sign-detection
    \end{lstlisting}
    
    \item Set up the environment and install dependencies:
    \begin{lstlisting}[language=bash]
    pip install -r requirements.txt
    \end{lstlisting}
    
    \item Run the main script:
    \begin{lstlisting}[language=bash]
    python main.py
    \end{lstlisting}
\end{enumerate}

\subsection{Conclusion}

This project seamlessly combines machine learning classification, geometric feature extraction, and clustering to achieve accurate road sign detection and localization from point clouds. By following the workflow and setup instructions, you can apply this pipeline to your own point cloud data and enhance road safety through improved road sign identification.

For detailed code snippets, see the provided \href{https://www.notion.so/scripts/}{scripts} folder.

\subsection{Contributing}

Contributions are welcome! Please feel free to open issues and pull requests to enhance this project further.

\subsection{License}

This project is licensed under the \href{https://www.notion.so/LICENSE}{MIT License}.

---

By \href{https://github.com/emilybrereton}{@emilybrereton}}
```

Please note that LaTeX rendering may vary depending on the platform and document class you're using. Additionally, some adjustments might be needed based on your specific LaTeX document settings.
