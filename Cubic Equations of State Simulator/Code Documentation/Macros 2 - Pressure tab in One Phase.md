# "Pressure" tab in "One Phase.xlsm" file

This spreadsheet allows performing calculations with the simulator results or experimental data of the thermodynamic properties in the liquid or vapor phase of an isobar.

## 1. Spreadsheet Design

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/macros2-1.jpg" width="1074" height="322">

*Figure 1. Spreadsheet Design of "Pressure" tab in "One Phase.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/macros2-2.jpg" width="948" height="474">

*Figure 2. Controls properties.*

## 2. Excel Macro Code

```vbscript
Private Sub CLEAN_4_Click()
    Dim row As Integer ' Helper to pass rows
    FUGACITY_TEST_4.Enabled = True
    FUGACITY_TEST_4.Value = True
    EXPERIMENTAL_DATA_4.Enabled = True
    COMPUTE_4.Enabled = True
    CLEAN_4.Enabled = False
    With Workbooks("One Phase.xlsm").Worksheets("Pressure")
        .Range("B3:B10").Value = ""
        .Range("G16").Value = ""
        .Range("R16").Value = ""
        .Range("A7").Value = "Reference Temperature"
        .Range("A8").Value = "Reference Pressure"
        .Range("A9").Value = "Reference Enthalpy"
        .Range("A10").Value = "Reference Entropy"
        .Range("G4").Value = "EoS Simulator"
        .Range("H19").Value = "U"
        .Range("H20").Value = "A"
        .Range("H21").Value = "G"
        .Range("S19").Value = "U"
        .Range("S20").Value = "A"
        .Range("S21").Value = "G"
        .Range("M4").Value = "T"
        .Range("G16").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="=ISBLANK(G16)"
            .IgnoreBlank = True
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        .Range("R16").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="=ISBLANK(R16)"
            .IgnoreBlank = True
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        row = 0
        While .Cells(14 + row, 1).Value <> ""
            .Range(Cells(14 + row, 1), Cells(14 + row, 5)).Value = ""
            .Range(Cells(14 + row, 1), Cells(14 + row, 5)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            Selection.Borders(xlEdgeLeft).LineStyle = xlNone
            Selection.Borders(xlEdgeBottom).LineStyle = xlNone
            Selection.Borders(xlEdgeRight).LineStyle = xlNone
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
            row = row + 1
        Wend
        row = 0
        While .Cells(14 + row, 12).Value <> ""
            .Range(Cells(14 + row, 12), Cells(14 + row, 16)).Value = ""
            .Range(Cells(14 + row, 12), Cells(14 + row, 16)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            Selection.Borders(xlEdgeLeft).LineStyle = xlNone
            Selection.Borders(xlEdgeBottom).LineStyle = xlNone
            Selection.Borders(xlEdgeRight).LineStyle = xlNone
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
            row = row + 1
        Wend
        .Range("A13:E13").Value = ""
        .Range("L13:P13").Value = ""
        .Range("G14:J14").Value = ""
        .Range("R14:U14").Value = ""
        .Range("G15").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-6]:R[-1]C[-6]<=R[1]C[0],R[-1]C[-6]:R[-1]C[-6])))"
        .Range("H15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-7]:R[-1]C[-3],3,FALSE),""-"")"
        .Range("I15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-8]:R[-1]C[-4],4,FALSE),""-"")"
        .Range("J15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-9]:R[-1]C[-5],5,FALSE),""-"")"
        .Range("G17").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MAX(IF(R[-3]C[-6]:R[-3]C[-6]<=R[-1]C[0],R[-3]C[-6]:R[-3]C[-6])))"
        .Range("H17").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-7]:R[-3]C[-3],3,FALSE),""-"")"
        .Range("I17").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-8]:R[-3]C[-4],4,FALSE),""-"")"
        .Range("J17").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-9]:R[-3]C[-5],5,FALSE),""-"")"
        .Range("R15").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-6]:R[-1]C[-6]<=R[1]C[0],R[-1]C[-6]:R[-1]C[-6])))"
        .Range("S15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-7]:R[-1]C[-3],3,FALSE),""-"")"
        .Range("T15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-8]:R[-1]C[-4],4,FALSE),""-"")"
        .Range("U15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-9]:R[-1]C[-5],5,FALSE),""-"")"
        .Range("R17").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MAX(IF(R[-3]C[-6]:R[-3]C[-6]<=R[-1]C[0],R[-3]C[-6]:R[-3]C[-6])))"
        .Range("S17").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-7]:R[-3]C[-3],3,FALSE),""-"")"
        .Range("T17").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-8]:R[-3]C[-4],4,FALSE),""-"")"
        .Range("U17").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-9]:R[-3]C[-5],5,FALSE),""-"")"
        .Columns("A:U").EntireColumn.AutoFit
        .Columns("B:U").ColumnWidth = 16.71
        .Range("A3").Select
    End With
End Sub

Private Sub COMPUTE_4_Click()
    Dim row_liquid As Integer ' Number of rows of liquid data
    Dim row_vapor As Integer ' Number of rows of vapor data
    Dim Tfactor As Double ' Temperature conversion factor
    Dim Pfactor As Double ' Pressure conversion factor
    Dim Vfactor As Double ' Volume conversion factor
    Dim Hfactor As Double ' Enthalpy conversion factor
    Dim Sfactor As Double ' Entropy conversion factor
    If FUGACITY_TEST_4.Value = True Then
        ' Check if it is possible to export results
        If Workbooks("One Phase.xlsm").Worksheets("Pressure").Range("A14") <> "" Or Workbooks("One Phase.xlsm").Worksheets("Pressure").Range("L14") <> "" Then
            MsgBox "Information is found in the data area.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1") <> Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1") Or Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1") Or Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1") Then
            MsgBox "The value of COMPOUND does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") <> Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") Or Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") Or Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") Then
            MsgBox "The value of CUBIC EQUATION OF STATE does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B3") <> Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B3") Or Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") Or Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B2") Then
            MsgBox "The value of ISOBAR PRESSURE [BAR] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B4") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B4") Then
            MsgBox "The value of REFERENCE STATE does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B5") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B5") Then
            MsgBox "The value of REFERENCE TEMPERATURE [K] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B6") <> Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B6") Then
            MsgBox "The value of REFERENCE PRESSURE [BAR] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("A13") <> "Liquid" Or Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("A13") <> "Liquid" Then
            MsgBox "Case thermodynamically not possible and there are no results in enthalpy and entropy calculations.", vbExclamation
            Exit Sub
        End If
        With Workbooks("One Phase.xlsm").Worksheets("Pressure")
            ' Export results
            If .Range("G4").Value = "EoS Simulator" Then
                Tfactor = 1
                Pfactor = 1
                Vfactor = 1
                Hfactor = 1
                Sfactor = 1
                .Range("A7").Value = "Reference Temperature [K]"
                .Range("A8").Value = "Reference Pressure [bar]"
                .Range("A9").Value = "Reference Enthalpy [kJ/kg]"
                .Range("A10").Value = "Reference Entropy [kJ/kg/K]"
                .Range("H19").Value = "U [kJ/kg]"
                .Range("H20").Value = "A [kJ/kg]"
                .Range("H21").Value = "G [kJ/kg]"
                .Range("S19").Value = "U [kJ/kg]"
                .Range("S20").Value = "A [kJ/kg]"
                .Range("S21").Value = "G [kJ/kg]"
                If .Range("M4").Value = "T" Then
                    .Range("D6:H6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("D7:H7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("D8:H8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("D9:H9").Select
                End If
                Selection.Copy
                .Range("A13").Select
                .Paste
                .Range("L13").Select
                .Paste
                If .Range("M4").Value = "T" Then
                    .Range("F6:H6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("F7:H7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("F8:H8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("F9:H9").Select
                End If
                Selection.Copy
                .Range("H14").Select
                .Paste
                .Range("S14").Select
                .Paste
                If .Range("M4").Value = "T" Then
                    .Range("D6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("D7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("D8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("D9").Select
                End If
                Selection.Copy
                .Range("G14").Select
                .Paste
                .Range("R14").Select
                .Paste
            Else
                Tfactor = 1.8
                Pfactor = 14.50377377
                Vfactor = 16.01846337
                Hfactor = 0.429922614
                Sfactor = 0.238845897
                .Range("A7").Value = "Reference Temperature [R]"
                .Range("A8").Value = "Reference Pressure [psia]"
                .Range("A9").Value = "Reference Enthalpy [BTU/lbm]"
                .Range("A10").Value = "Reference Entropy [BTU/lbm/R]"
                .Range("H19").Value = "U [BTU/lbm]"
                .Range("H20").Value = "A [BTU/lbm]"
                .Range("H21").Value = "G [BTU/lbm]"
                .Range("S19").Value = "U [BTU/lbm]"
                .Range("S20").Value = "A [BTU/lbm]"
                .Range("S21").Value = "G [BTU/lbm]"
                If .Range("M4").Value = "T" Then
                    .Range("I6:M6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("I7:M7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("I8:M8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("I9:M9").Select
                End If
                Selection.Copy
                .Range("A13").Select
                .Paste
                .Range("L13").Select
                .Paste
                If .Range("M4").Value = "T" Then
                    .Range("K6:M6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("K7:M7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("K8:M8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("K9:M9").Select
                End If
                Selection.Copy
                .Range("H14").Select
                .Paste
                .Range("S14").Select
                .Paste
                If .Range("M4").Value = "T" Then
                    .Range("I6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("I7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("I8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("I9").Select
                End If
                Selection.Copy
                .Range("G14").Select
                .Paste
                .Range("R14").Select
                .Paste
            End If
            .Range("B3:B4").Value = Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B1:B2").Value
            .Range("B5").Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B3").Value) * Pfactor
            .Range("B6").Value = Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B4").Value
            .Range("B7").Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B5").Value) * Tfactor
            .Range("B8").Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B6").Value) * Pfactor
            .Range("B9").Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B7").Value) * Hfactor
            .Range("B10").Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Range("B7").Value) * Sfactor
            ' Liquid
            row_liquid = 0
            While Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 1).Value = "Liquid"
                If .Range("M4").Value = "T" Then
                    .Cells(14 + row_liquid, 1).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 2).Value) * Tfactor
                    .Cells(14 + row_liquid, 2).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 3).Value
                    .Cells(14 + row_liquid, 3).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 4).Value) * Vfactor
                    .Cells(14 + row_liquid, 4).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Hfactor
                    .Cells(14 + row_liquid, 5).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Sfactor
                ElseIf .Range("M4").Value = "V" Then
                    .Cells(14 + row_liquid, 3).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 2).Value) * Tfactor
                    .Cells(14 + row_liquid, 2).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 3).Value
                    .Cells(14 + row_liquid, 1).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 4).Value) * Vfactor
                    .Cells(14 + row_liquid, 4).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Hfactor
                    .Cells(14 + row_liquid, 5).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Sfactor
                ElseIf .Range("M4").Value = "H" Then
                    .Cells(14 + row_liquid, 4).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 2).Value) * Tfactor
                    .Cells(14 + row_liquid, 2).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 3).Value
                    .Cells(14 + row_liquid, 3).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 4).Value) * Vfactor
                    .Cells(14 + row_liquid, 1).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Hfactor
                    .Cells(14 + row_liquid, 5).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Sfactor
                ElseIf .Range("M4").Value = "S" Then
                    .Cells(14 + row_liquid, 5).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 2).Value) * Tfactor
                    .Cells(14 + row_liquid, 2).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 3).Value
                    .Cells(14 + row_liquid, 3).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(5 + row_liquid, 4).Value) * Vfactor
                    .Cells(14 + row_liquid, 4).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Hfactor
                    .Cells(14 + row_liquid, 1).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(13 + row_liquid, 4).Value) * Sfactor
                End If
                row_liquid = row_liquid + 1
            Wend
            ' Vapor
            row_vapor = 0
            While Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 1).Value = "Vapor"
                If .Range("M4").Value = "T" Then
                    .Cells(14 + row_vapor, 12).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 2).Value) * Tfactor
                    .Cells(14 + row_vapor, 13).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 3).Value
                    .Cells(14 + row_vapor, 14).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 4).Value) * Vfactor
                    .Cells(14 + row_vapor, 15).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Hfactor
                    .Cells(14 + row_vapor, 16).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Sfactor
                ElseIf .Range("M4").Value = "V" Then
                    .Cells(14 + row_vapor, 14).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 2).Value) * Tfactor
                    .Cells(14 + row_vapor, 13).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 3).Value
                    .Cells(14 + row_vapor, 12).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 4).Value) * Vfactor
                    .Cells(14 + row_vapor, 15).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Hfactor
                    .Cells(14 + row_vapor, 16).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Sfactor
                ElseIf .Range("M4").Value = "H" Then
                    .Cells(14 + row_vapor, 15).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 2).Value) * Tfactor
                    .Cells(14 + row_vapor, 13).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 3).Value
                    .Cells(14 + row_vapor, 14).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 4).Value) * Vfactor
                    .Cells(14 + row_vapor, 12).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Hfactor
                    .Cells(14 + row_vapor, 16).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Sfactor
                ElseIf .Range("M4").Value = "S" Then
                    .Cells(14 + row_vapor, 16).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 2).Value) * Tfactor
                    .Cells(14 + row_vapor, 13).Value = Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 3).Value
                    .Cells(14 + row_vapor, 14).Value = CDbl(Workbooks("Isobar given Pressure on a TV Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(11 + row_liquid + row_vapor, 4).Value) * Vfactor
                    .Cells(14 + row_vapor, 15).Value = CDbl(Workbooks("Isobar given Pressure on a TH Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Hfactor
                    .Cells(14 + row_vapor, 12).Value = CDbl(Workbooks("Isobar given Pressure on a TS Diagram.xlsm").Worksheets("Isobar given Pressure").Cells(19 + row_liquid + row_vapor, 4).Value) * Sfactor
                End If
                row_vapor = row_vapor + 1
            Wend
            ' Format
            ' Liquid
            .Range(Cells(14, 1), Cells(13 + row_liquid, 5)).Select
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlBottom
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlCenter
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlInsideVertical)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            With Selection.Borders(xlInsideHorizontal)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            .Range(Cells(13, 1), Cells(13 + row_liquid, 1)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            ' Vapor
            .Range(Cells(14, 12), Cells(13 + row_vapor, 16)).Select
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlBottom
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlCenter
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlInsideVertical)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            With Selection.Borders(xlInsideHorizontal)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            .Range(Cells(13, 12), Cells(13 + row_vapor, 12)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
            ' Liquid
            .Range("G15").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-6]:R[" & row_liquid - 2 & "]C[-6]<=R[1]C[0],R[-1]C[-6]:R[" & row_liquid - 2 & "]C[-6])))"
            .Range("H15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-7]:R[" & row_liquid - 2 & "]C[-3],3,FALSE),""-"")"
            .Range("I15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-8]:R[" & row_liquid - 2 & "]C[-4],4,FALSE),""-"")"
            .Range("J15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-9]:R[" & row_liquid - 2 & "]C[-5],5,FALSE),""-"")"
            .Range("G17").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-6]:R[" & row_liquid - 4 & "]C[-6]>=R[-1]C[0],R[-3]C[-6]:R[" & row_liquid - 4 & "]C[-6])))"
            .Range("H17").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-7]:R[" & row_liquid - 4 & "]C[-3],3,FALSE),""-"")"
            .Range("I17").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-8]:R[" & row_liquid - 4 & "]C[-4],4,FALSE),""-"")"
            .Range("J17").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-9]:R[" & row_liquid - 4 & "]C[-5],5,FALSE),""-"")"
            .Range("G16").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                :=xlBetween, Formula1:="=MIN(A14:A" & 13 + row_liquid & ")", Formula2:="=MAX(A14:A" & 13 + row_liquid & ")"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            ' Vapor
            .Range("R15").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-6]:R[" & row_vapor - 2 & "]C[-6]<=R[1]C[0],R[-1]C[-6]:R[" & row_vapor - 2 & "]C[-6])))"
            .Range("S15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-7]:R[" & row_vapor - 2 & "]C[-3],3,FALSE),""-"")"
            .Range("T15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-8]:R[" & row_vapor - 2 & "]C[-4],4,FALSE),""-"")"
            .Range("U15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-9]:R[" & row_vapor - 2 & "]C[-5],5,FALSE),""-"")"
            .Range("R17").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-6]:R[" & row_vapor - 4 & "]C[-6]>=R[-1]C[0],R[-3]C[-6]:R[" & row_vapor - 4 & "]C[-6])))"
            .Range("S17").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-7]:R[" & row_vapor - 4 & "]C[-3],3,FALSE),""-"")"
            .Range("T17").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-8]:R[" & row_vapor - 4 & "]C[-4],4,FALSE),""-"")"
            .Range("U17").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-9]:R[" & row_vapor - 4 & "]C[-5],5,FALSE),""-"")"
            .Range("R16").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                :=xlBetween, Formula1:="=MIN(L14:L" & 13 + row_vapor & ")", Formula2:="=MAX(L14:L" & 13 + row_vapor & ")"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Columns("A:U").EntireColumn.AutoFit
            .Columns("C:U").ColumnWidth = 16.71
            .Range("A3").Select
        End With
    Else
        With Workbooks("One Phase.xlsm").Worksheets("Pressure")
            ' Check if it is possible to use experimental data
            If .Range("B3") = "" Then
                MsgBox "The value of COMPOUND is empty.", vbExclamation
                Exit Sub
            End If
            If .Range("B5") = "" Then
                If Workbooks("One Phase.xlsm").Worksheets("Temperature").Range("G4").Value = "EoS Simulator" Then
                    MsgBox "The value of ISOBAR PRESSURE [BAR] is empty.", vbExclamation
                Else
                    MsgBox "The value of ISOBAR PRESSURE [PSIA] is empty.", vbExclamation
                End If
                Exit Sub
            End If
            If .Range("A14") = "" And .Range("L14") = "" Then
                MsgBox "No experimental data presented.", vbExclamation
                Exit Sub
            End If
            If .Range("G4").Value = "EoS Simulator" Then
                .Range("A7").Value = "Reference Temperature [K]"
                .Range("A8").Value = "Reference Pressure [bar]"
                .Range("A9").Value = "Reference Enthalpy [kJ/kg]"
                .Range("A10").Value = "Reference Entropy [kJ/kg/K]"
                .Range("H19").Value = "U [kJ/kg]"
                .Range("H20").Value = "A [kJ/kg]"
                .Range("H21").Value = "G [kJ/kg]"
                .Range("S19").Value = "U [kJ/kg]"
                .Range("S20").Value = "A [kJ/kg]"
                .Range("S21").Value = "G [kJ/kg]"
                If .Range("M4").Value = "T" Then
                    .Range("D6:H6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("D7:H7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("D8:H8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("D9:H9").Select
                End If
                Selection.Copy
                If .Range("A14") <> "" Then
                    .Range("A13").Select
                    .Paste
                End If
                If .Range("L14") <> "" Then
                    .Range("L13").Select
                    .Paste
                End If
                If .Range("M4").Value = "T" Then
                    .Range("F6:H6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("F7:H7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("F8:H8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("F9:H9").Select
                End If
                Selection.Copy
                If .Range("A14") <> "" Then
                    .Range("H14").Select
                    .Paste
                End If
                If .Range("L14") <> "" Then
                    .Range("S14").Select
                    .Paste
                End If
                If .Range("M4").Value = "T" Then
                    .Range("D6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("D7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("D8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("D9").Select
                End If
                Selection.Copy
                If .Range("A14") <> "" Then
                    .Range("G14").Select
                    .Paste
                End If
                If .Range("L14") <> "" Then
                    .Range("R14").Select
                    .Paste
                End If
            Else
                .Range("A7").Value = "Reference Temperature [R]"
                .Range("A8").Value = "Reference Pressure [psia]"
                .Range("A9").Value = "Reference Enthalpy [BTU/lbm]"
                .Range("A10").Value = "Reference Entropy [BTU/lbm/R]"
                .Range("H19").Value = "U [BTU/lbm]"
                .Range("H20").Value = "A [BTU/lbm]"
                .Range("H21").Value = "G [BTU/lbm]"
                .Range("S19").Value = "U [BTU/lbm]"
                .Range("S20").Value = "A [BTU/lbm]"
                .Range("S21").Value = "G [BTU/lbm]"
                If .Range("M4").Value = "T" Then
                    .Range("I6:M6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("I7:M7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("I8:M8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("I9:M9").Select
                End If
                Selection.Copy
                If .Range("A14") <> "" Then
                    .Range("A13").Select
                    .Paste
                End If
                If .Range("L14") <> "" Then
                    .Range("L13").Select
                    .Paste
                End If
                If .Range("M4").Value = "T" Then
                    .Range("K6:M6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("K7:M7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("K8:M8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("K9:M9").Select
                End If
                Selection.Copy
                If .Range("A14") <> "" Then
                    .Range("H14").Select
                    .Paste
                End If
                If .Range("L14") <> "" Then
                    .Range("S14").Select
                    .Paste
                End If
                If .Range("M4").Value = "T" Then
                    .Range("I6").Select
                ElseIf .Range("M4").Value = "V" Then
                    .Range("I7").Select
                ElseIf .Range("M4").Value = "H" Then
                    .Range("I8").Select
                ElseIf .Range("M4").Value = "S" Then
                    .Range("I9").Select
                End If
                Selection.Copy
                If .Range("A14") <> "" Then
                    .Range("G14").Select
                    .Paste
                End If
                If .Range("L14") <> "" Then
                    .Range("R14").Select
                    .Paste
                End If
            End If
            .Range("B4").Value = "-"
            .Range("B6:B10").Value = "-"
            ' Liquid
            If .Range("A14") <> "" Then
                row_liquid = 0
                While .Cells(14 + row_liquid, 1) <> ""
                    row_liquid = row_liquid + 1
                Wend
                ' Format
                .Range(Cells(14, 1), Cells(13 + row_liquid, 5)).Select
                With Selection
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlBottom
                    .WrapText = False
                    .Orientation = 0
                    .AddIndent = False
                    .IndentLevel = 0
                    .ShrinkToFit = False
                    .ReadingOrder = xlContext
                    .MergeCells = False
                End With
                With Selection
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                    .WrapText = False
                    .Orientation = 0
                    .AddIndent = False
                    .IndentLevel = 0
                    .ShrinkToFit = False
                    .ReadingOrder = xlContext
                    .MergeCells = False
                End With
                Selection.Borders(xlDiagonalDown).LineStyle = xlNone
                Selection.Borders(xlDiagonalUp).LineStyle = xlNone
                With Selection.Borders(xlEdgeLeft)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeTop)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeBottom)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeRight)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlInsideVertical)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlThin
                End With
                With Selection.Borders(xlInsideHorizontal)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlThin
                End With
                .Range(Cells(13, 1), Cells(13 + row_liquid, 1)).Select
                Selection.Borders(xlDiagonalDown).LineStyle = xlNone
                Selection.Borders(xlDiagonalUp).LineStyle = xlNone
                With Selection.Borders(xlEdgeLeft)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeTop)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeBottom)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeRight)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                Selection.Borders(xlInsideVertical).LineStyle = xlNone
                ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
                .Range("G15").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-6]:R[" & row_liquid - 2 & "]C[-6]<=R[1]C[0],R[-1]C[-6]:R[" & row_liquid - 2 & "]C[-6])))"
                .Range("H15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-7]:R[" & row_liquid - 2 & "]C[-3],3,FALSE),""-"")"
                .Range("I15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-8]:R[" & row_liquid - 2 & "]C[-4],4,FALSE),""-"")"
                .Range("J15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-9]:R[" & row_liquid - 2 & "]C[-5],5,FALSE),""-"")"
                .Range("G17").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-6]:R[" & row_liquid - 4 & "]C[-6]>=R[-1]C[0],R[-3]C[-6]:R[" & row_liquid - 4 & "]C[-6])))"
                .Range("H17").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-7]:R[" & row_liquid - 4 & "]C[-3],3,FALSE),""-"")"
                .Range("I17").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-8]:R[" & row_liquid - 4 & "]C[-4],4,FALSE),""-"")"
                .Range("J17").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-9]:R[" & row_liquid - 4 & "]C[-5],5,FALSE),""-"")"
                .Range("G16").Select
                With Selection.Validation
                    .Delete
                    .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                    :=xlBetween, Formula1:="=MIN(A14:A" & 13 + row_liquid & ")", Formula2:="=MAX(A14:A" & 13 + row_liquid & ")"
                    .IgnoreBlank = True
                    .InCellDropdown = True
                    .InputTitle = ""
                    .ErrorTitle = ""
                    .InputMessage = ""
                    .ErrorMessage = ""
                    .ShowInput = True
                    .ShowError = True
                End With
            End If
            ' Vapor
            If .Range("L14") <> "" Then
                row_vapor = 0
                While .Cells(14 + row_vapor, 12) <> ""
                    row_vapor = row_vapor + 1
                Wend
                ' Format
                .Range(Cells(14, 12), Cells(13 + row_vapor, 16)).Select
                With Selection
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlBottom
                    .WrapText = False
                    .Orientation = 0
                    .AddIndent = False
                    .IndentLevel = 0
                    .ShrinkToFit = False
                    .ReadingOrder = xlContext
                    .MergeCells = False
                End With
                With Selection
                    .HorizontalAlignment = xlCenter
                    .VerticalAlignment = xlCenter
                    .WrapText = False
                    .Orientation = 0
                    .AddIndent = False
                    .IndentLevel = 0
                    .ShrinkToFit = False
                    .ReadingOrder = xlContext
                    .MergeCells = False
                End With
                Selection.Borders(xlDiagonalDown).LineStyle = xlNone
                Selection.Borders(xlDiagonalUp).LineStyle = xlNone
                With Selection.Borders(xlEdgeLeft)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeTop)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeBottom)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeRight)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlInsideVertical)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlThin
                End With
                With Selection.Borders(xlInsideHorizontal)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlThin
                End With
                .Range(Cells(13, 12), Cells(13 + row_vapor, 12)).Select
                Selection.Borders(xlDiagonalDown).LineStyle = xlNone
                Selection.Borders(xlDiagonalUp).LineStyle = xlNone
                With Selection.Borders(xlEdgeLeft)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeTop)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeBottom)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                With Selection.Borders(xlEdgeRight)
                    .LineStyle = xlContinuous
                    .Color = -8762076
                    .TintAndShade = 0
                    .Weight = xlMedium
                End With
                Selection.Borders(xlInsideVertical).LineStyle = xlNone
                ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
                .Range("R15").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-6]:R[" & row_vapor - 2 & "]C[-6]<=R[1]C[0],R[-1]C[-6]:R[" & row_vapor - 2 & "]C[-6])))"
                .Range("S15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-7]:R[" & row_vapor - 2 & "]C[-3],3,FALSE),""-"")"
                .Range("T15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-8]:R[" & row_vapor - 2 & "]C[-4],4,FALSE),""-"")"
                .Range("U15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-9]:R[" & row_vapor - 2 & "]C[-5],5,FALSE),""-"")"
                .Range("R17").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-6]:R[" & row_vapor - 4 & "]C[-6]>=R[-1]C[0],R[-3]C[-6]:R[" & row_vapor - 4 & "]C[-6])))"
                .Range("S17").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-7]:R[" & row_vapor - 4 & "]C[-3],3,FALSE),""-"")"
                .Range("T17").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-8]:R[" & row_vapor - 4 & "]C[-4],4,FALSE),""-"")"
                .Range("U17").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-9]:R[" & row_vapor - 4 & "]C[-5],5,FALSE),""-"")"
                .Range("R16").Select
                With Selection.Validation
                    .Delete
                    .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                    :=xlBetween, Formula1:="=MIN(L14:L" & 13 + row_vapor & ")", Formula2:="=MAX(L14:L" & 13 + row_vapor & ")"
                    .IgnoreBlank = True
                    .InCellDropdown = True
                    .InputTitle = ""
                    .ErrorTitle = ""
                    .InputMessage = ""
                    .ErrorMessage = ""
                    .ShowInput = True
                    .ShowError = True
                End With
            End If
            .Columns("A:U").EntireColumn.AutoFit
            .Columns("C:U").ColumnWidth = 16.71
            .Range("A3").Select
        End With
    End If
    FUGACITY_TEST_4.Enabled = False
    EXPERIMENTAL_DATA_4.Enabled = False
    COMPUTE_4.Enabled = False
    CLEAN_4.Enabled = True
End Sub
```